import re

def strip_punctuation_ru(data):
    return re.sub(r'[^\w\s]', '', data).strip()
