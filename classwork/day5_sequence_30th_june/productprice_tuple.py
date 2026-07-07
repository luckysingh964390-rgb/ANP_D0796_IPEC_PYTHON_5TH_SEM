print("Enter any 5 prices of products :")
list = []

for i in range(5):
    # taking input from user :
    price = float(input("Enter the price of product : "))
    name = input("Enter the name of the product: ")
    # appending the price to the list:
    list.append({"name": name, "price": price})

# displaying the list :
print("List is :",list)

tpl = tuple(list)

# displaying the tuple:
print("Tuple is :",tpl)

count = 0
for item in range(len(tpl)):
    if tpl[item]["price"] > 4000:
        count = count + 1
    min_price = min(tpl[item]["price"])
    max_price = max(tpl[item]["price"])
    
print("Minimum price is :",min_price)
print("Maximum price is :",max_price)

print("Number of products with price greater than 4000 is :",count)