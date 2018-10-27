import re

WORD = r'\b\w+\b'
PUNCTUATION = r'[.!?]'
OTHER_NON_WORDS = r'\W'
TOKEN_RE = re.compile('|'.join([WORD, PUNCTUATION, OTHER_NON_WORDS]))

def split(sentence):
    tokens = []
    found = TOKEN_RE.search(sentence)
    while found:
        token = sentence[0:found.end()]
        if token != '' and token != ' ':
            tokens.append(token)
        sentence = sentence[found.end():]
        found = TOKEN_RE.search(sentence)
    
    return tokens

def tokenize(sentence):
    return split(sentence) 
