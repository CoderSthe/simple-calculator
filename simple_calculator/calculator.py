def add(*args):
    total = 0
    for num in args:
        total += num
    return total


def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total


def subtract(num1, *args):
    total = num1
    for num in args:
        if num < 0:
            total -= (-num)
        else:
            total = total - num
    return total


def divide(num1, *args):
    total = num1
    for num in args:
        total /= num
    return total
