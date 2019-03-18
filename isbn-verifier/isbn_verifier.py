import string


def verify(isbn):
    digits = [d for d in isbn if d in string.digits + 'X']
    if len(digits) != 10:
        return False
    digits[-1] = '10' if digits[-1] == 'X' else digits[-1]
    multiples = [(10 - i) * int(d) for i, d in enumerate(digits)]
    return sum(multiples) % 11 == 0
