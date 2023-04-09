"""Else & Finally"""

try:
    n1 = int(input("Type first number: "))
except Exception as e:
    print("An error has ocurred.")
else:
    print("All good!")
finally:
    print('I believe I can fly!')
