#write a program to find 3rd largest number in a list or 20 numbers given by user
numbers = []
for i in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Find the 3rd largest number
numbers.sort(reverse=True)
third_largest = numbers[2]
print("The 3rd largest number is:", third_largest)


