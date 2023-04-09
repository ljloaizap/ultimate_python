"""Class properties"""


class Dog:
    paws = 4

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def speak(self):
        print(f"Guau! (I'm {self.name}!)")


Dog.paws = 3
my_dog = Dog("Rocu", 12)
my_dog.paws = 5
# my_dog.speak()
print(Dog.paws)
print(my_dog.paws)
