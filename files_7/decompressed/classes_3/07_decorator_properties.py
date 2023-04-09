class Dog:

    def __init__(self, name) -> None:
        self.name = name

    @property
    def name(self):
        print('running getter')
        return self.__name

    @name.setter
    def name(self, name):
        print('running setter')
        if name.strip():
            self.__name = name
        return


dog = Dog("Lolo")
print(dog.name)
