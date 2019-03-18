def is_leap_year(year):
    def is_devided(num):
        return year % num == 0
    return is_devided(400) or (is_devided(4) and not is_devided(100))
