n = int(input("Enter number of employees: "))

salary = []

for i in range(n):
    s = int(input("Enter salary: "))
    salary.append(s)

highest = max(salary)
lowest = min(salary)
average = sum(salary) / n

count = 0
for s in salary:
    if s > 50000:
        count += 1

print("Highest Salary =", highest)
print("Lowest Salary =", lowest)
print("Average Salary =", average)
print("Employees earning more than 50000 =", count)