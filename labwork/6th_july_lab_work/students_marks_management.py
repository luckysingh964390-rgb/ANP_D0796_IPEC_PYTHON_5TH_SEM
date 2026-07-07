#Create a dictionary to store the marks of 5 students, where the key is the student's name and the value is their marks.
students = {}

# Input names and marks
for i in range(5):
    name = input(f"Enter the name of student {i + 1}: ")
    marks = int(input(f"Enter marks of {name}: "))
    students[name] = marks

# Display the dictionary
print("\nStudent Marks Dictionary:")
print(students)