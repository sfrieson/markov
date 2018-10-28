import re
import cleanup
import prepare
import random
import markov_tokenize as tokenize

START = '_START_'
END = '_END_'

LEFT_JOIN_PUNCTUATION = re.compile(r"['’”,]")
RIGHT_JOIN_PUNCTUATION = re.compile(r"[“]")
CONTEXTUAL_JOIN_PUNCTUATION = re.compile(r'["]')

def make_pairs(tokens, pairs):
    """
    Makes the Markov pairs from a list of tokens
    """

    if START not in pairs:
        pairs = {START: []}

    for idx, token in enumerate(tokens):
        if idx is 0:
            pairs[START].append(token)
        next_idx = idx + 1

        try:
            key = pairs[token]
        except KeyError:
            key = pairs[token] = []

        try:
            key.append(tokens[next_idx])
        except IndexError:
            pairs[token].append(END)

    return pairs

def select_element(list):
    """
    Selects an element from the list for the next link in the Markov chain generated sentence.
    """
    return random.choice(list)

def prepare_data(paragraphs):
    sentences = []
    for paragraph in paragraphs:
        sentences = sentences + prepare.prepare(cleanup.clean(paragraph))

    model = {}
    for sentence in sentences:
        model = make_pairs(tokenize.tokenize(sentence), model)

    return model

def join_chain(chain):
    CAPITALIZED = False
    sentence = ''
    chain = iter(chain)

    try:
        # Punctuation might come before first word
        while not CAPITALIZED:
            link = next(chain)
            if re.match(r'^\w', link):
                link = link.capitalize()
                CAPITALIZED = True
            sentence += link

        while True:
            ADD_SPACE_BEFORE = True
            link = next(chain)
            previous_character = sentence[len(sentence) - 1]

            if LEFT_JOIN_PUNCTUATION.match(link):
                ADD_SPACE_BEFORE = False
                
            if RIGHT_JOIN_PUNCTUATION.match(previous_character):
                ADD_SPACE_BEFORE = False
            
            if ADD_SPACE_BEFORE:
                sentence += ' '

            sentence += link
    except StopIteration:
        pass
    return sentence

def generate(pairs):
    last_word = '_START_'
    
    chain = []
    while last_word is not '_END_':
        word = select_element(pairs[last_word])
        if word is not '_END_':
            chain.append(word)
        last_word = word

    return join_chain(chain)
