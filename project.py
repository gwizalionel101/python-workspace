
account = {
    "name": "Lionel",
    "balance": 50500,
    "PIN": "12345",
    "type": "adminaccount"
}

print("=== MINI ATM ===")

pin = input("Enter your PIN: ")

if pin == account["PIN"]:

    while True:
        print("\n*** ATM MENU ***")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Account Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is:", account["balance"])

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                account["balance"] += amount
                print("Money deposited successfully.")
                print("New balance:", account["balance"])
            else:
                print("Amount must be greater than zero.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > account["balance"]:
                print("Insufficient balance.")
            else:
                account["balance"] -= amount
                print("Please collect your cash.")
                print("New balance:", account["balance"])

        elif choice == "4":
            print("\nAccount Name:", account["name"])
            print("Account Balance:", account["balance"])
            print("Account Type:", account["type"])

        elif choice == "5":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Invalid PIN")
    print("Access Denied")
