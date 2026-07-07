#Write a Python program that defines a function search_student(student_dict, roll_no).
def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"


students = {
    101: "Rahul",
    102: "Priya",
    103: "Ankit",
    104: "Neha",
    105: "Aman"
}

roll_no = int(input("Enter Roll Number: "))

result = search_student(students, roll_no)

print(result)