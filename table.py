
import pandas

data = {
    "Name": ["ARSENE", "Bob", "Lionel"],
    "Age": [10, 30, 15],
    "salary": [1000, 2000, 3000],
    "city": ["New York", "Los Angeles", "Chicago"]
}

df = pandas.DataFrame(data)

while True:
    print("----EMPLOYEES MANAGER----")
    print("1. Display all employees")
    print("2. Search employees by city")
    print("3. Sort employees by salary")
    print("4. Add a new employee")
    print("5. Exit")

    choice = input("Choose an option: ")
    print()

    if choice == "1":
        print(df)

    elif choice == "2":
        place = input("Enter city name: ")
        result = df[df["city"] == place]

        if result.empty:
            print("No employees found in", place)
        else:
            print(result)

    elif choice == "3":
        new = df.sort_values("salary", ascending=False)
        print(new)

    elif choice == "4":
        n = input("Enter employee name: ")
        a = int(input("Enter employee age: "))
        s = float(input("Enter employee salary: "))
        c = input("Enter employee city: ")

        df.loc[len(df)] = [n, a, s, c]
        print("Employee added successfully!")

    elif choice == "5":
        print("Thank you for using the Employees Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again!")

    print()
