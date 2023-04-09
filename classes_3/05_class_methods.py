"""Class methods"""


class Dog:
    paws = 4

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    @classmethod
    def speak(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        """Like 'dogs by default'"""
        return cls("Chachito feliz", 4)


Dog.speak()
dog1 = Dog("Chachito", 2)
dog2 = Dog("Felipe", 3)

dog3 = Dog.factory()
print(dog3.name, dog3.age)
