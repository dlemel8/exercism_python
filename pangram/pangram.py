import string


def is_pangram(s):
    input_letters = [c for c in s.lower() if c in string.ascii_lowercase]
    return len(string.ascii_lowercase) == len(set(input_letters))
