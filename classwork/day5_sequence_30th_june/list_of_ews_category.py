# Create lists to store names and salaries
names = []
salaries = []

# Accept details of 15 persons
for i in range(15):
    name = input(f"Enter name of Person {i + 1}: ")
    salary = float(input(f"Enter annual salary (in LPA) of {name}: "))

    names.append(name)
    salaries.append(salary)

# Display persons eligible for EWS category
print("\nPersons Eligible for EWS Category (Salary < 5 LPA):")

for i in range(15):
    if salaries[i] < 5:
        print(names[i])