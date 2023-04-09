class Bird:
    def __init__(self):
        print('Bird constructor')
        self.flies = True

    def fly(self):
        print('Fly, bird!')


class Duck(Bird):
    def __init__(self):
        print('Duck constructor')
        self.swims = True
        super().__init__()

    def fly(self):
        print('Duck, bird!')
        super().fly()


duck = Duck()
duck.fly()
print(duck.flies, duck.swims)
