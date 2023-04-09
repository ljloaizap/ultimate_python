# class Animal:

#     def eat(self):
#         print('Eating')

#     def walk(self):
#         print('Animals walking')


# class Dog:

#     def walk(self):
#         print('Dog Walking')


# class Chanchito(Animal, Dog):

#     def coding(self):
#         print('Coding')


# Chanchito().walk()


"""Other samples"""


class Walker:
    def walk(self):
        print('Walking')


class Flyer:
    def fly(self):
        print('Flying')


class Swimer:
    def swim(self):
        print('Swimming')


class Duck(Flyer, Swimer, Walker):
    def speak(self):
        print('Duck!')


duck = Duck()
duck.swim()
duck.walk()
duck.fly()
