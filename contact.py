 #CONTACT BOOK
print()
print("===THIS IS ABOUT CONTACT BOOK===")
contacts = {}
while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully.")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated.")
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "5":
        for name, phone in contacts.items():
            print(name, ":", phone)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")