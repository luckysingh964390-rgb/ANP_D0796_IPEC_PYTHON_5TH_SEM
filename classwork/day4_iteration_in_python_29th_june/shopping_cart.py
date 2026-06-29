# Enter number of products
n = int(input("Enter number of products: "))

total = 0

# Input price of each product
for i in range(n):
    price = float(input("Enter price of product: "))
    total = total + price

# Display bill
print("\nShopping Cart Bill")
print("Total Amount =", total)

# Discount (optional)
if total > 5000:
    discount = total * 0.10
    print("Discount =", discount)
    print("Final Amount =", total - discount)
else:
    print("No Discount")