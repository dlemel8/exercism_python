def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('must be same length')

    res = 0
    for a, b in zip(strand_a, strand_b):
        res += 0 if a == b else 1
    return res
