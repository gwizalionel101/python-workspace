  #LIST SEARCH
print()
print("===THIS IS ABOUT LIST SEARCH===")
numbers = [10, 20, 30, 20, 40, 20, 50]
value = int(input("Enter the value to search for: "))
positions = []
for i in range(len(numbers)):
    if numbers[i] == value:
        positions.append(i)
if positions:
    print("Value found at positions:", positions)
else:
    print("Value not found.")


    #EVEN COMPREHENSION
print()
print("===THIS ABOUT LIST COMPREHENSION===")
squares = [n ** 2 for n in range(1, 101) if n % 2 == 0]
print(squares)
   

    #ODD COMPREHENSION
print("===THIS ABOUT LIST COMPREHENSION ON ODDS===")
squares=[ n ** 2 for n in range(1,101) if n % 2 !=0]
print(squares)

  
    #MATRIX ADDITION
print()
print("===THE MATRIX ADDITION===")
matrix1 = [[1, 2, 3],[4, 5, 6]]
matrix2 = [[7, 8, 9],[10, 11, 12]]
result = []
for i in range(len(matrix1)):
    row = []
    for j in range(len(matrix1[0])):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("Sum of matrices:")
for row in result:
    print(row)


    #MATRIX TRANSPOSE
print()
print("===THIS ABOUT MATRIX TRANSPOSE===")
matrix = [[1, 2, 3],[4, 5, 6]]
transpose = []
for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transpose:
    print(row)


    #TUPLE BASED RECORDS
print()
print("===THIS IS ABOUT TUPLE BASED RECORDS===")
employees = [
    (101, "Alice", "Manager", 500000),
    (102, "John", "Developer", 350000),
    (103, "Mary", "Accountant", 300000)
]
for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Position:", employee[2])
    print("Salary:", employee[3])
    print("--------------------")


    #SET OPERATIONS
print()
print("===THIS ABOUT SET OPERATIONS===")
students_a = {101, 102, 103, 104, 105}
students_b = {104, 105, 106, 107, 108}

print("Union:", students_a | students_b)
print("Intersection:", students_a & students_b)
print("Difference (A - B):", students_a - students_b)
print("Symmetric difference:", students_a ^ students_b)


     #WORD FREQUENCY DICTIONARY
print()
print("===THIS IS ABOUT WORD FREQUENCY DICTIONARY===")
paragraph = input("Enter a paragraph: ")
words = paragraph.lower().split()
frequency = {}
for word in words:
    word = word.strip(".,!?;:")
    if word != "":
        frequency[word] = frequency.get(word, 0) + 1
print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)


   
# CONTACT BOOK

print()
print("=== THIS IS ABOUT CONTACT BOOK ===")

contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()
    if choice == "1":
        name = input("Enter name: ").strip()
        if name == "":
            print("Name cannot be empty.")
        elif name in contacts:
            print("This contact already exists.")
        else:
            phone = input("Enter phone number: ").strip()

            if phone == "":
                print("Phone number cannot be empty.")
            else:
                contacts[name] = phone
                print("Contact added successfully.")
    elif choice == "2":
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print("Name:", name)
            print("Phone number:", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Enter name to update: ").strip()
        if name in contacts:
            phone = input("Enter new phone number: ").strip()
            if phone == "":
                print("Phone number cannot be empty.")
            else:
                contacts[name] = phone
                print("Contact updated successfully.")
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == "5":
        if len(contacts) == 0:
            print("Your contact book is empty.")
        else:
            print("\n--- ALL CONTACTS ---")
            for name, phone in contacts.items():
                print(name, ":", phone)
            print("Total contacts:", len(contacts))
    elif choice == "6":
        print("Thank you for using the Contact Book!")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose from 1 to 6.")



        #INVENTORY DICTIONARY
print()
print("===THIS ABOUT INVENTORY DICTIONARY===")
inventory = {
    "Laptop": {"quantity": 5, "price": 500000},
    "Phone": {"quantity": 10, "price": 200000},
    "Keyboard": {"quantity": 8, "price": 15000}
}
total_value = 0
for product, details in inventory.items():
    quantity = details["quantity"]
    price = details["price"]
    value = quantity * price
    print("Product:", product)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total value:", value)
    print("--------------------")
    total_value += value
print("Total inventory value:", total_value)


      #MERGE DICTIONARIES
print()
print("===THIS ABOUT MERGING DICTIONARIES===")
dictionary1 = {
    "name": "Alice",
    "age": 20,
    "city": "Kigali"
}
dictionary2 = {
    "age": 22,
    "country": "Rwanda",
    "course": "Programming"
}
merged = dictionary1.copy()
merged.update(dictionary2)
print("First dictionary:", dictionary1)
print("Second dictionary:", dictionary2)
print("Merged dictionary:", merged)


      #SORT DICTIONARY RECORDS
print()
print("===THIS ABOUT SORTING DICTIONARIES=== ")
students = {
    "Alice": 85,
    "John": 72,
    "Mary": 95,
    "Peter": 68,
    "David": 90
}
sorted_students = sorted(
    students.items(),
    key=lambda item: item[1],
    reverse=True
)
print("Students sorted by marks:")
for name, marks in sorted_students:
    print(name, ":", marks)