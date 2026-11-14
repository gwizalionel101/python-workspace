#THIS IS ABOUT EXERCISE 21
print("THIS IS ABOUT EXERCISE 21")
print("TO FIND IF SOMEONE IS ELIGIBLE TO VOTE")
name=input("Enter your Fullname:")
age=int(input("Enter your age:"))
if age>=18:
  print("Eligible to vote!")
else :
  print("Not eligible to vote")

#THIS IS ABOUT EXERCISE 22
print("THIS ABOUT MULTIPLICATION NUMBER OF ANY NUMBER")
nbr=int(input("Provide a number :"))
print("The multiplication table of this  provided number is:")
number=[1,2,3,4,5,6,7,8,9,10,11,12]
for a in number:
  result=nbr*a
  print(f"{nbr}*{a}={result}")
print("would you like more multiplication tables? (yes/no)")
if input() == "yes":
  nbr=int(input("Provide a number :"))
  print("The multiplication table of this  provided number is:")
  number=[1,2,3,4,5,6,7,8,9,10,11,12]
  for a in number:
    result=nbr*a
    print(f"{nbr}*{a}={result}")
else :
  print("Thank you for using this program !")


#THIS ABOUT DEFAULT PARAMETERS
def me(name,greeting="Hello"):
  return name + " " + greeting
print(me("John"))
print(me("John", "Good morning"))


#THIS ABOUT EXERCISE 23
number=int(input("Enter the number of your choice:"))
print(" === THE SUM OF THE NATURAL NUMBER IS === ")
print("Pease consider the last sentence !")
tt=0
h=range(0,number+1)
for m in h:
  tt= tt + m
print(f"The sum of the natural numbers from 0 to {number}is :{tt}")


#THIS ABOUT EXERCISE 29
print("THIS IS ABOUT PRINTING A DIAMOND")
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*",end="")
    print()


#THIS IS ABOUT DIAMOND
print("THIS IS ABOUT PRINTING DIAMOND")
rows = int(input("Enter the number of rows: "))  #taking input from user
for i in range(1,rows+1):
  print(" "*(rows-i) + "*"*(2*i-1))  #here i is the current row number and remember that the last number in range dont count it
for i in range(rows-1,0,-1):
  print(" "*(rows-i) + "*"*(2*i-1))  #here i is the current row number

#THIS ABOUT EXERCISE 30
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

    
  #THIS IS ABOUT EXERCISE 31
std=[89,90,65,78,80,97,94,65,55,40]
tt=sum(std)
length=len(std)
avg=tt/length
hg=max(std)
lw=min(std)
print("the total marks:",tt)
print("the average marks:",avg)
print("the highest mark:",hg)
print("the lowest mark:",lw)


#THIS IS ABOUT EXERCISE 32
print("TO REMOVE THE SAME NUMBER IN THE LIST AND STAY ONLY WITH ONLY ONE ")
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print("Original list:", numbers)
print("List without duplicates:", unique_numbers)


#THIS IS ABOUT EXERCISE 33
#non returning functions
def greet():
    print("Hello!")
greet()

#multiplying the numbers
def multiply(*params):
    return params
args=multiply(1,2,3,4,5)
result = 1
for n in args:
    result *= n
print(result)

#subtacting the numbers
def subtract(*params):
    return params[0] - sum(params[1:])
print(subtract(10, 1, 2, 3))


count = 1
while count <= 5:
  print(count)
  count += 1
