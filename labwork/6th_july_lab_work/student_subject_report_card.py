#Create a nested dictionary to store marks of students in three subjects.
students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 88},
    "Priya": {"Math": 78, "Science": 95, "English": 82},
    "Ankit": {"Math": 91, "Science": 89, "English": 94}
}

topper = ""
highest = 0

for name in students:
    total = sum(students[name].values())
    average = total / 3

    print(name)
    print("Total =", total)
    print("Average =", average)

    if total > highest:
        highest = total
        topper = name

print("Topper =", topper)

subjects = ["Math", "Science", "English"]

for subject in subjects:
    max_marks = 0
    student = ""

    for name in students:
        if students[name][subject] > max_marks:
            max_marks = students[name][subject]
            student = name

    print(subject, "Highest =", max_marks, "by", student)

print("Students with average >= 85")

for name in students:
    average = sum(students[name].values()) / 3
    if average >= 85:
        print(name)