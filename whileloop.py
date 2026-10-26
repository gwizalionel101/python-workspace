password = ""
while password != "1234":
    password = input("Enter password: ")
    if password == "1234":
        print("Login successful!")
    else:
        print("Wrong password. Try again!")
print("Welcome to the application!")

