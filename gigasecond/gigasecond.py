from datetime import timedelta

import math


def add_gigasecond(birth_date):
    return birth_date + timedelta(seconds=math.pow(10.0, 9))
