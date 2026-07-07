#create a tuple of 10 products with their prices and display the lowest and highest price products and count the number of product which is grester thsn 4000 along with the price you required to store the name of product also while displaying lowest price and highest price display the name of product along with there name and price
products  = [("computer", 50000), ("Laptop", 40000), ("Mobile", 30000), ("Tablet", 20000), ("Headphones", 5000), ("Keyboard", 2000), ("Mouse", 1000), ("Monitor", 15000), ("Printer", 8000), ("Speaker", 6000)]

# Find the product with the lowest price
lowest_price_product = min(products, key=lambda x: x[1])
# Find the product with the highest price
highest_price_product = max(products, key=lambda x: x[1])

# Count the number of products with price greater than 4000
count_greater_than_4000 = sum(1 for product in products if product[1] > 4000)

# Display the results
print(f"Lowest price product: {lowest_price_product[0]} - ${lowest_price_product[1]}")
print("Highest price product: {highest_price_product[0]} - ${highest_price_product[1]}")
print("Number of products with price greater than 4000: {count_greater_than_4000}")