from Product import Product

class Electronics(Product):
    def __init__(self, product_Id: str, name: str, base_Price: float, warranty_period: int):
        super().__init__(product_Id, name, base_Price)
        self.warranty_period = warranty_period

    def calculate_Final_Price(self) -> float:
        # Assuming warranty adds a fixed cost of $10 per month
        return self.base_Price + (self.warranty_period * 10)