class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product {self.name} costs ${self.price}"


class Category:
    products = []

    def __init__(self, name, products) -> None:
        self.name = name
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def print_prod(self):
        for product in self.products:
            print(product)


kayak = Product("Kayak", 1000)
bicycle = Product("Bicycle", 750)
surfboard = Product("Surfboard", 500)

sports = Category("Sports", [kayak, bicycle])
sports.add_product(surfboard)
sports.print_prod()
