import string


def is_isogram(s):
    input_letters = [c for c in s.lower() if c in string.ascii_lowercase]
    return len(input_letters) == len(set(input_letters))
