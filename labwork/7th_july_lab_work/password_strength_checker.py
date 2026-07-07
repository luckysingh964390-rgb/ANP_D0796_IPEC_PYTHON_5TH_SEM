#Write a function check_password(password) that checks whether a password is strong.
def check_password(password):
    if len(password) < 8:
        return "Weak Password"

    upper = False
    lower = False
    digit = False

    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True

    if upper and lower and digit:
        return "Strong Password"
    else:
        return "Weak Password"

password = input("Enter password: ")

print(check_password(password))