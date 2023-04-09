"""Exceptions type"""

try:
    n1 = int(input("Type first number: "))
    # adww
except ValueError as e:
    print("You have to type a numeric entry")
except NameError as e:
    print("Name error, uhm...")
