username = "gwiza"
email = "gwiza@gmail.com"
password = "123"
while True:
    um = input("Enter username: ")
    em = input("Enter email: ")
    pw = input("Enter password: ")
    if um != username or em == email or pw == password:
      print("invalid username")
    if um == username and em == email and pw == password:
        print("Welcome to my app!")
        break
    elif um == username and em != email and pw != password:
        print("Invalid email and password")
    elif um == username and em != email:
        print("Please check your email")
    elif um == username and em == email and pw != password:
        print("Invalid password")
    else:
        print("Incorrect login details. Try again.")
