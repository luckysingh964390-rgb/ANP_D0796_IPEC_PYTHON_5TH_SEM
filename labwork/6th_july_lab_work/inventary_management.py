#Create a dictionary to maintain the stock of products in a shop.
# Dictionary of products and their stock
stock = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# Display all products
print("Current Stock:")
print(stock)

# Add a new product
name = input("\nEnter new product name: ")
qty = int(input("Enter stock: "))
stock[name] = qty

# Update stock
name = input("\nEnter product name to update: ")
if name in stock:
    stock[name] = int(input("Enter new stock: "))
else:
    print("Product not found!")

# Remove product
name = input("\nEnter product name to remove: ")
if name in stock:
    del stock[name]
    print("Product removed.")
else:
    print("Product not found!")

# Products having stock less than 20
print("\nProducts with stock less than 20:")
for product, qty in stock.items():
    if qty < 20:
        print(product, ":", qty)

# Total items in inventory
total = sum(stock.values())
print("\nTotal items in inventory:", total)