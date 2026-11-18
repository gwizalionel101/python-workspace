try:
    # Code that might cause an error
except:
    # Code that runs if an error occurs

#1st EXAMPLE
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except:
    print("Something went wrong!")


#2nd EXAMPLE
#HERE YOU SPECIFY THE TYPE OF ERROR
#different types of errors inlude{}
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Please enter numbers only!")
except ZeroDivisionError:
    print("You cannot divide by zero!")

#3rd EXAMPLE
#WHEN YOU USE ELSE
try:
    num = int(input("Enter a number: "))
except ValueError:#here is when error occurs
    print("Invalid input!")
else:#if no error occurs
    print("Your number is:", num)


#4th EXAMPLE 
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
finally:#it executesalways even if the program have errors
    print("Program finished!")

#DIFFERENT ERRORS
#SyntaxError	Incorrect Python syntax
#IndentationError	Incorrect indentation
#NameError	Using a variable that doesn't exist
#TypeError	Using an operation on an incompatible data type
#ValueError	Correct data type but invalid value
#ZeroDivisionError	Dividing by zero
#IndexError	Accessing a list index that doesn't exist
#KeyError	Accessing a dictionary key that doesn't exist
#AttributeError	Using an attribute or method that doesn't exist
#FileNotFoundError	File does not exist
#ModuleNotFoundError	Module cannot be found
#ImportError	Import operation fails
#RuntimeError	General runtime error
#RecursionError	Maximum recursion depth exceeded
#OverflowError	Numeric operation produces a result too large
#MemoryError	Not enough memory
#OSError	Operating system-related error
#PermissionError	Insufficient permission to access a resource
#IsADirectoryError	Trying to use a directory as a file
#NotADirectoryError	A path component is not a directory
#EOFError	Input operation reaches the end of a file unexpectedly
#StopIteration	An iterator has no more items
#AssertionError	An assertion condition is false
#FloatingPointError	Floating-point operation error
#UnicodeError	Unicode encoding or decoding error
#ConnectionError	Network connection-related error
#TimeoutError	An operation takes too long
#BrokenPipeError	Attempting to write to a broken pipe
#KeyboardInterrupt	User interrupts program execution
#SystemError	Internal interpreter error