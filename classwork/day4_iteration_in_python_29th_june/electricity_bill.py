# Accept number of houses
n = int(input("Enter the number of houses: "))

units = []

# Accept units consumed by each house
for i in range(n):
    unit = int(input(f"Enter units consumed by House {i + 1}: "))
    units.append(unit)

# Calculations
total = sum(units)
average = total / n
highest = max(units)
lowest = min(units)

# Display results
print("\nElectricity Bill Analysis")
print("Total units consumed =", total)
print("Average units consumed =", average)
print("Highest consumption =", highest)
print("Lowest consumption =", lowest)