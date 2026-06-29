while True:
    password = input("Enter a password: ")
    if len(password) >= 8:
        print("password Accepted.")
        break
    else:
        print("password to short.")
