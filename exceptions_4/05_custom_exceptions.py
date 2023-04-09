"""Custom exceptions"""


class CustomError(Exception):
    "This class represents my error."

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f"[Err {self.code}]: {self.message}"


def divide(n=0):
    if n == 0:
        raise CustomError("Cannot devide by 0, dude.", "805")
    return 5 / n


try:
    divide()
except CustomError as e:
    print(e)
