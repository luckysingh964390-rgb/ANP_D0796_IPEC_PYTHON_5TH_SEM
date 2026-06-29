# Enter number of students
n = int(input("Enter number of students: "))

marks = []

# Input marks
for i in range(n):
    m = int(input("Enter marks of student: "))
    marks.append(m)

# Calculations
highest = max(marks)
lowest = min(marks)
average = sum(marks) / n

passed = 0
failed = 0

for m in marks:
    if m >= 40:
        passed += 1
    else:
        failed += 1

# Display results
print("\nStudent Result Analysis")
print("Highest Marks =", highest)
print("Lowest Marks =", lowest)
print("Average Marks =", average)
print("Number of Passed Students =", passed)
print("Number of Failed Students =", failed)