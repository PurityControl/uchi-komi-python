def to(limit):
    def is_divisible(number):
        return number % 3 == 0 or number % 5 == 0

    return sum([number for number in range(1, limit) if is_divisible(number)])

