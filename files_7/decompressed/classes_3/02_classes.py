"""Classes"""


class Dog:

    def speak(self):
        print("Guau!")


my_dog = Dog()
print(type(my_dog))
my_dog.speak()

print(isinstance(my_dog, Dog))
print(isinstance(my_dog, str))
