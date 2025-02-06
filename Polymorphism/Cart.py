from Product import Product

class Cart:
    def __init__(self):
        self.products = []

    def add_Product(self, product: Product):
        self.products.append(product)

    def calculateTotalPrice(self) -> float:
        total = 0
        for product in self.products:
            total += product.calculate_Final_Price()
        return total