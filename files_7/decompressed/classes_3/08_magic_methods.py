"""Magic methods"""


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"🐍 Chao perro: {self.name}")

    def __str__(self):
        return f"Dog class: {self.name}"

    def speak(self):
        print(f"{self.name} says: Guau!")


dog = Dog("Bella", 14)
print(dog)

# text = str(dog)
# print(text)

del dog  # actually needed?
