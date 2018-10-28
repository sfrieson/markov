import re

ENDING_PUNCTUATION = r'[.?!]'
SENTENCE_DELIMITER = ENDING_PUNCTUATION + ' '

def split_paragraph(paragraph):
    """
    Returns a paragraph as a list of sentences. 
    """
    sentences = []
    found = re.search(SENTENCE_DELIMITER, paragraph)
    while found:
        sentences.append(paragraph[0:found.end() - 1])
        paragraph = paragraph[found.end():]
        found = re.search(SENTENCE_DELIMITER, paragraph)

    sentences.append(paragraph)
    return sentences

def prepare(str):
    return split_paragraph(str)
