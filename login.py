username1="lionel"
password1="12345"
username2="gwiza"
password2="54321"
username3="mucyo"
password3="67890"

un= input("Enter username: ")
pw= input("Enter password: ")

if un== username1:
    if pw==password1:
        print("Login successful!")
        print("Welcome, Admin!")
    else:
        print("Incorrect password!")

elif un==username2:
    if pw==password2:
        print("Login successful!")
        print("Welcome!")
    else:
        print("Incorrect password!")

elif username == username3:
    if pw==password3:
        print("Login successful!")
        print("Welcome!")
    else:
        print("Incorrect password!")

else:
    print("Username not found!")

