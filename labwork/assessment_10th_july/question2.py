#create a python program that stores employee details in a dictionary.

emp = {}

for i in range(5):
    eid = input("Enter ID: ")
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))
    emp[eid] = {"Name": name, "Salary": salary}

print("\n Employee Details")

total = 0
high = 0
high_name = ""

for id in emp:
    print(id, emp[id]["Name"], emp[id]["Salary"])

    total += emp[id]["Salary"]

    if emp[id]["Salary"] > high:
        high = emp[id]["Salary"]
        high_name = emp[id]["Name"]

print("\n Highest Salary")
print(high_name, high)

print("\n Average Salary")
print(total / 5)