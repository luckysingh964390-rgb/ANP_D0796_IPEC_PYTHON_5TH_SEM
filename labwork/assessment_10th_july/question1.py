#write a python program that performs the following tasks:

def calculate(marks):
    total = sum(marks)
    per = total / 5
    return total, per

name = input("Enter Name: ")

marks = []
for i in range(5):
    m = int(input("Enter Marks: "))
#append marks
    marks.append(m)

total, per = calculate(marks)

if per >= 90:
    grade = "A+"
elif per >= 75:
    grade = "A"
elif per >= 60:
    grade = "B"
elif per >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Student Name :", name)
print("Marks :", marks)
print("Total :", total)
print("Percentage :", per)
print("Grade :", grade)