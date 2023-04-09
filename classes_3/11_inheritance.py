class Animal:

    def eat(self):
        print('Eating')


class Dog(Animal):

    def walk(self):
        print('Walking')


class Chanchito(Animal):

    def coding(self):
        print('Coding')


class ChanchitoWeird(Dog):

    def coding(self):
        print('Coding')


dog = Dog()
dog.walk()
dog.eat()

chanchito = Chanchito()
chanchito.coding()
chanchito.eat()

# Multiple inheritance
chanchito_weird = ChanchitoWeird()
chanchito_weird.walk()
