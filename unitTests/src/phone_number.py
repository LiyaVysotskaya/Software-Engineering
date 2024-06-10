import re

def is_correct_mobile_phone_number_ru(number):
    pattern = r"^(8|\+7)\s*\(?\d{3}\)?\s*\d{3}[-\s]?\d{2}[-\s]?\d{2}$"
    return re.match(pattern, number) is not None
