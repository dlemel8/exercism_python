import re
from collections import Counter

VALID_WORD_RE = re.compile("([a-zA-Z0-9']+)")


def word_count(phrase):
    words = (w.strip("'\"") for w in VALID_WORD_RE.findall(phrase.lower()))
    return Counter(words)
