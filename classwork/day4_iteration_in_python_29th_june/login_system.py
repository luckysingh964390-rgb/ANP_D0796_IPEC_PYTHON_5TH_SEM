# Correct username and password
username = "admin"
password = "1234"

attempt = 1

while attempt <= 3:
    u = input("Enter Username: ")
    p = input("Enter Password: ")

    if u == username and p == password:
        print("Login Successful")
        break
    else:
        print("Invalid Username or Password")
        attempt = attempt + 1

if attempt > 3:
    print("Maximum attempts reached. Login Failed.")