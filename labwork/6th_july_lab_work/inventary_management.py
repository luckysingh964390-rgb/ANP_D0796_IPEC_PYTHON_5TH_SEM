#Create a dictionary to maintain the stock of products in a shop.
stock = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# Add
stock["Printer"] = 20

# Update
stock["Laptop"] = 18

# Remove
del stock["Monitor"]

# Stock less than 20
print("Stock less than 20:")
for i in stock:
    if stock[i] < 20:
        print(i)

# Total items
print("Total Items =", sum(stock.values()))