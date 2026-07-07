#Create a dictionary where:
# Employee ID is the key.
# Value is another dictionary containing employee details such as name, age, and department.
# Employee Dictionary

employees = {}

n = int(input("Enter number of employees: "))

for i in range(n):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = {
        "Name": name,
        "Department": dept,
        "Salary": salary
    }

# Display all employees
print("\nEmployee Details")
for emp_id in employees:
    print(emp_id, employees[emp_id])

# Search employee
search = input("\nEnter Employee ID to search: ")

if search in employees:
    print(employees[search])
else:
    print("Employee not found")

# Increase salary by 10%
for emp_id in employees:
    employees[emp_id]["Salary"] *= 1.10

print("\nUpdated Salary")
for emp_id in employees:
    print(emp_id, employees[emp_id])

# Employees of a department
dept = input("\nEnter Department: ")

print("Employees in", dept)
for emp_id in employees:
    if employees[emp_id]["Department"].lower() == dept.lower():
        print(emp_id, employees[emp_id]["Name"])