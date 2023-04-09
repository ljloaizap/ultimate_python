"""Invoke exceptions"""


def divide(n=0):
    if n == 0:
        raise ZeroDivisionError("Cannot devide by 5, dude.", 1, False)
    return 5 / n


try:
    divide()
except ZeroDivisionError as e:
    print(e)
