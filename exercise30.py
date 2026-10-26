while True:
    print()
    print("=== MENU-DRIVEN CALCULATOR ===")
    print("1. Addition\n2. Subtraction\n3.multiplication\n4.division\n5.exit")
    choice = int(input("Choose an option : "))
    if choice == 1:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        print("Result:", n1 + n2)
    elif choice == 2:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        print("Result:", n1 - n2)
    elif choice == 3:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        print("Result:", n1 * n2)
    elif choice == 4:
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        if n2 == 0:
           print("Error: It is not divide by zero!")
        else:
           print(f"The result of {n1}/{n2}:",n1/n2)
    elif choice == 5:
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid choice! Please choose between 1 and 5.")

