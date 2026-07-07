#Create a nested dictionary to store marks of students in three subjects, where the key is the student's name and the value is another dictionary containing subject names as keys and their corresponding marks as values.
students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Priya": {"Math": 78, "Science": 95, "English": 82},
    "Ankit": {"Math": 91, "Science": 89, "English": 94}
}

top = ""
high = 0

for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    avg = total / 3
    print(name, "Total =", total, "Average =", avg)

    if total > high:
        high = total
        top = name

print("Topper =", top)

print("Math Highest =", max(students, key=lambda x: students[x]["Math"]))
print("Science Highest =", max(students, key=lambda x: students[x]["Science"]))
print("English Highest =", max(students, key=lambda x: students[x]["English"]))

print("Average >= 85")
for name in students:
    total = students[name]["Math"] + students[name]["Science"] + students[name]["English"]
    if total / 3 >= 85:
        print(name)