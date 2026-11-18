def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)
    print("The length is:",len(args))
names = []
while True:
    print("\nEnter your choice")
    print("1. Append list")
    print("2. Print answer")
    choice = int(input("Enter your choice: "))
    if choice == 2:
        print("Thank you!")
        break
    if choice == 1:
        name = input("Enter name: ")
        names.append(name)
if len(names) >= 2:
    my_function(*names)
else:
    print("Please enter at least two names.")