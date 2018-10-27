import re

special_characters = {
    '...': '…'
}
def replace_special_characters(str):
    for target in special_characters:
        str = str.replace(target, special_characters[target])

    return str

def remove_extra_spaces(str):
    return re.sub(r'\s+', ' ', str)

def clean(str):
    return replace_special_characters(remove_extra_spaces(str))