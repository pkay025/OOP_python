from abc import ABC, abstractmethod

class Product:
    def __init__(self, product_Id: str, name: str, base_Price: float):
        self.product_Id = product_Id
        self.product_Name = name
        self.base_Price = base_Price

    def apply_Discount(self, percentage: float):
        self.base_Price -= self.base_Price * (percentage / 100)

    @abstractmethod
    def calculate_Final_Price(self) -> float:
        pass

    