while True:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    option = input("Enter your option: ")
    if option == 'addition':
        print("ADDITION:", n1 + n2)
    elif option == 'subtraction':
        print("SUBTRACTION:", n1 - n2)
    elif option == 'multiplication':
        print("MULTIPLICATION:", n1 * n2)
    elif option == 'division':
        if n2 == 0:
            print("Impossible: division by zero")
            continue
        else:
            print("DIVISION:", n1 / n2)
    elif option == "all":
        print("ADDITION:", n1 + n2)
        print("SUBTRACTION:", n1 - n2)
        print("MULTIPLICATION:", n1 * n2)
        if n2 == 0:
            print("DIVISION: Impossible")
        else:
            print("DIVISION:", n1 / n2)
    else:
        print("Invalid option")
        continue

    break
