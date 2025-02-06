from Product import Product

class Clothing(Product):
    def __init__(self, product_Id: str, name: str, base_Price: float, size: str, fabric_charge: float):
        super().__init__(product_Id, name, base_Price)
        self.size = size
        self.fabric_charge = fabric_charge

    def calculate_Final_Price(self) -> float:
        return self.base_Price + self.fabric_charge