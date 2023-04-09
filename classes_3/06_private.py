"""Private properties"""


class Dog:

    def __init__(self, name, age) -> None:
        self.__name = name
        self.age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def speak(self):
        print(f"{self.__name} says: Guau!")

    @classmethod
    def factory(cls):
        """Like 'dogs by default'"""
        return cls("Chachito feliz", 4)


dog1 = Dog.factory()
dog1.speak()

# print(dog1.__name) # -> error
print(dog1.__dict__)  # Don't do this. Lol.
# print(dog1._Dog__name)
