#write a python program that repeatedly asks the user to enter a password until is satisfies #all the following conditions
 
def check_password(password):
    if len(password) < 8:
        return False

    upper = False
    lower = False
    digit = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True

    return upper and lower and digit

#enter the password
while True:
    password = input("Enter Password: ")

    if check_password(password):
        print("Password Accepted")
        break
    else:
        print("Invalid Password")