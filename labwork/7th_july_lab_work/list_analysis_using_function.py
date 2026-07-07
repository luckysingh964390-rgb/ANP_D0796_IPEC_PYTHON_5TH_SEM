#write a python program that defines the following functions:
#find_maximum(numbers):
#find_minimum(numbers): 
#find_average(numbers):
def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_average(numbers):
    return sum(numbers) / len(numbers)

numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Maximum =", find_max(numbers))
print("Minimum =", find_min(numbers))
print("Average =", find_average(numbers))