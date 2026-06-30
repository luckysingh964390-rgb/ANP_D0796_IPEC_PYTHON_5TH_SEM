# Create lists to store names and marks
names = []
marks = []

# Accept details of 50 students
for i in range(50):
    name = input(f"Enter name of Student {i + 1}: ")
    mark = int(input(f"Enter marks of {name}: "))

    names.append(name)
    marks.append(mark)

# Display eligible students
print("\nStudents Eligible for Admission (Marks > 75):")

for i in range(50):
    if marks[i] > 75:
        print(names[i])