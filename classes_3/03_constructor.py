"""Class constructor"""


class Dog:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def speak(self):
        print(f"Guau! (I'm {self.name}!)")


my_dog = Dog("Rocu", 12)
my_dog.speak()
