#Write a Python program that defines a function calculate_grade(marks).
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

for i in range(5):
    marks = int(input("Enter marks: "))
    grade = calculate_grade(marks)
    print("Marks =", marks)
    print("Grade =", grade)