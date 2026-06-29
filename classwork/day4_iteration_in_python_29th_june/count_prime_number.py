# Accept starting and ending values
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

count = 0

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")
            count += 1

print("\nTotal prime numbers =", count)