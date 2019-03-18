import re

YELL_RE = re.compile('^[^a-z]*[A-Z]{2,}[^a-z]*$')
QUESTION_RE = re.compile('^.*\?\s*$')
NOTHING_RE = re.compile('^\s*$')


def hey(phrase):
    yell, question, nothing = [r.match(phrase) for r in [YELL_RE, QUESTION_RE, NOTHING_RE]]
    if yell and question:
        return "Calm down, I know what I'm doing!"
    if yell:
        return 'Whoa, chill out!'
    if question:
        return 'Sure.'
    if nothing:
        return 'Fine. Be that way!'
    return 'Whatever.'
