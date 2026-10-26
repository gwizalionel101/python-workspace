    #QUESTION 46
print("===REUSABLE CALCULATOR FUNCTIONS===")
print() 
def me(a,b):
  return a+b
def he(a,b):
  return a-b
def she(a,b):
  return a*b
def you(a,b):
  if b==0:
    print("Cannot be divided by zero")
  return a/b
a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
print("___________________________________________")
print("ADDITION:",me(a,b))
print("SUBTRACTION:",he(a,b))
print("MULTIPLLICATION:",she(a,b))
print("DIVISION:",you(a,b))


    #QUESTION 47
print("===FUNCTION PARAMETER===")
print()
def greet(name, greeting="Hello"):
    print(greeting, name)

greet("GWIZA")
greet("Lionel", "Good morning")



       #QUESTION48
print("===VARIABLE SCOPE ARGUMENTS===")
print()
def average(*numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    return total / len(numbers)
count = int(input("How many numbers do you want to enter? "))
numbers = []
for i in range(count):
    number = float(input("Enter a number: "))
    numbers.append(number)
result = average(*numbers)
print("The average is:", result)
