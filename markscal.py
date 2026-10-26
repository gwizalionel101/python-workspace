   #REUSABLE CALCULATOR FUNCTIONS

# 56. Student Class

class Student:
    def __init__(self, name, student_id, marks):
        self.name = name
        self.student_id = student_id
        self.marks = marks

    # Calculate average
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0

        return sum(self.marks) / len(self.marks)

    # Display student details
    def display_details(self):
        print("\n--- STUDENT DETAILS ---")
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())


# Get student information from the user
name = input("Enter student name: ")
student_id = input("Enter student ID: ")

marks = []
number = int(input("How many marks do you want to enter? "))

for i in range(number):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)

# Create student object
student1 = Student(name, student_id, marks)

# Display student details
student1.display_details()

