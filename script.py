import random
import re
# Some lines with some patterns I'm sure to come across.
file = [
    'This is the first line.',
    'This is the second line.  It has another line after it as well.',
    'Which line is this? It\'s the third line of course. ',
    'This is boring.',
    'No one invited you.',
    'Hey 7, why am I so afraid of you?',
    'BECAUSE I ATE 9!!!',
    '',
    'What happend to 9? Oh... 7 ate him. I get the joke...I think.',
    'What kind of "joke" is this?'
]

# Clean lines
def process(line):
    line = re.sub(r'\s+', ' ', line).lower().strip()
    
    # Not actually sure what should happen with punctuation yet.
    line = re.sub(r'[.?!][.?!\'"]*', '.', line)
    
    return line

clean_lines = [process(line) for line in file]

# print(clean_lines)

# split paragraphs into sentences

def split_paragraph(paragraph, all_sentences):
    sentences = re.split(r'\. ?', paragraph)
    if sentences[len(sentences) - 1] == '':
        sentences.pop()
    return all_sentences + sentences

all_sentences = []
for paragraph in clean_lines:
    all_sentences = split_paragraph(paragraph, all_sentences)

# tokenize
def tokenize(sentence):
    return sentence.split(' ')

tokenized = [tokenize(sentence) for sentence in all_sentences]

# Set up Markov pairs

def make_pairs(lists):
    pairs = {'_START_': []}

    for l in lists:
        for idx, word in enumerate(l):
            if idx is 0:
                pairs['_START_'].append(word)
            next_idx = idx + 1

            try:
                key = pairs[word]
            except KeyError:
                key = pairs[word] = []

            try:
                key.append(l[next_idx])
            except IndexError:
                pairs[word].append('_END_')

    return pairs

pairs = make_pairs(tokenized)

# ---

# Create a few sentences

def random_element(list):
    return random.choice(list)

def generate(pairs):
    last_word = '_START_'
    
    chain = []
    while last_word is not '_END_':
        word = random_element(pairs[last_word])
        if word is not '_END_':
            chain.append(word)
        last_word = word

    return ' '.join(chain) + '.'


print(generate(pairs))
print(generate(pairs))
print(generate(pairs))