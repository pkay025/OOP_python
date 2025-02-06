from Electronics import Electronics
from Clothing import Clothing
from Cart import Cart

# Create Products
laptop = Electronics("E001", "Laptop", 1000.0, 24)
jacket = Clothing("C001", "Winter Jacket", 200.0, "M", 20.0)

# Apply 10% discount to Laptop
laptop.apply_Discount(10)

# Calculate final price of Laptop and Winter Jacket
print(f"Laptop Final Price: {laptop.calculate_Final_Price()}")
print(f"Winter Jacket Final Price: {jacket.calculate_Final_Price()}")

# Add both to Cart and calculate total price
cart = Cart()
cart.add_Product(laptop)
cart.add_Product(jacket)
print(f"Total Cart Price: {cart.calculateTotalPrice()}")