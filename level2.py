#THIS IS ABOUT EXERCISE 11
print("THIS IS ABOUT EXERCISE 11")
sent=input("Enter a sentence:")
print("--------------------------------------------------------------------")
print("Sentence in uppercase:",sent.upper())
print("Sentence in lowercase:",sent.lower())
print("Sentence in lowercase:",sent.title())
  

#THIS IS ABOUT EXERCISE 12
print("THIS IS ABOUT EXERCISE 12")
m=(input("Scratch the sentence:"))
m=m.replace(" ","")
print("..................................................................")
print("This is the sentence without space:",m)
print(len(m))

#THIS ABOUT EXERCISE 13
print("THIS IS ABOUT EXERCISE 13")
frw=float(input("Enter the amount in FRW:"))
print(f"ENTER YOUR OPTION\n  1.in USD($)\n  2.in EURO(€)\n  3.in Kenyan shilling(KSh)\n  4.burundi francs(FBu)\n  5.in pound(£)\n  6.in DR CONGO(FC)")
option=int(input("Enter your option:"))
if option == 1:
  print("The currrency in USD:",frw/1473.00)
elif option == 2:
  print("The currency in EURO:",frw/1656.00)
elif option == 3:
  print("The currency in kenyan shilling:",frw/9.86)
elif option == 4:
  print("The currency in burundian currency is:",frw/0.491)
elif option == 5:
  print("The currency in pounds:",frw/1966.00)
elif option == 6:
  print("The currency in DRC(FC):",frw/0.651)
else :
  print("Invalid option")
  
  
#THIS IS ABOUT EXERCISE 14
print("THIS IS ABOUT EXERCISE 14")
print("=====THE RECEIPT FROM GWIZA SHOP=====")
pnm=input("Enter the product name:")
qu=float(input("Enter the product quantity:"))
ut=float(input("Enter the unit price per 1kg:"))
tt=qu*ut
vat=(tt*18)/100
print("============================================================")
print("Product name:",pnm)
print("The product quantity:",qu)
print("The unit price per 1kg:",ut)
print("The total to pay:",tt)
print("The value added tax (VAT)",vat)
print("============================================================")


#THIS IS ABOUT EXERCISE 15
print("THIS IS ABOUT EXERCISE 15")
   # 1. ARITHMETIC OPERATORS (+, -, *, /, %, **, //)
print("=== 1. Arithmetic Operators ===")
a = 15
b = 4
print(f"Addition ({a} + {b}):", a + b)
print(f"Subtraction ({a} - {b}):", a - b)
print(f"Multiplication ({a} * {b}):", a * b)
print(f"Division ({a} / {b}):", a / b)
print(f"Modulus/Remainder ({a} % {b}):", a % b)
print(f"Exponent/Power ({a} ** {b}):", a ** b)
print(f"Floor Division ({a} // {b}):", a // b)
print("-" * 30)
  # 2. COMPARISON OPERATORS (==, !=, >, <, >=, <=)
print("=== 2. Comparison Operators ===")
x = 10
y = 20
print(f"Is Equal To ({x} == {y}):", x == y)
print(f"Is Not Equal To ({x} != {y}):", x != y)
print(f"Greater Than ({x} > {y}):", x > y)
print(f"Less Than ({x} < {y}):", x < y)
print(f"Greater Than or Equal To ({x} >= {y}):", x >= y)
print(f"Less Than or Equal To ({x} <= {y}):", x <= y)
print("-" * 30)
  # 3. LOGICAL OPERATORS (and, or, not)
print("=== 3. Logical Operators ===")
has_id = True
is_adult = False
print(f"AND Logic (Both must be True): {has_id} and {is_adult} =", has_id and is_adult)
print(f"OR Logic (At least one must be True): {has_id} or {is_adult} =", has_id or is_adult)
print(f"NOT Logic (Inverts the value): not {is_adult} =", not is_adult)
print("-" * 30)
  # 4. ASSIGNMENT OPERATORS (=, +=, -=, *=, /=)
print("=== 4. Assignment Operators ===")
num = 5
print("Initial Assignment (num = 5):", num)
num += 3  # Equivalent to: num = num + 3
print("Add and Assign (num += 3):", num)
num -= 2  # Equivalent to: num = num - 2
print("Subtract and Assign (num -= 2):", num)
num *= 2  # Equivalent to: num = num * 2
print("Multiply and Assign (num *= 2):", num)
num /= 4  # Equivalent to: num = num / 4
print("Divide and Assign (num /= 4):", num)
print("-" * 30)
  # 5. MEMBERSHIP OPERATORS (in, not in)
print("=== 5. Membership Operators ===")
shopping_list = ["apple", "banana", "cherry"]

print("Is 'apple' in the list?", "apple" in shopping_list)
print("Is 'orange' in the list?", "orange" in shopping_list)
print("Is 'orange' NOT in the list?", "orange" not in shopping_list)


#THIS IS ABOUT EXERCISE 16
print("THIS IS ABOUT EXERCISE 16")
print("THIS IS ABOUT CHECKING WHETHER A NUMBER IS POSITIVE, NEGATIVE OR ZERO")
nbr = float(input("Enter the number you want to check: "))
if nbr > 0:
  print(f"This number {nbr} is positive.")
elif nbr == 0:
  print(f"This number {nbr} is zero.")
else:
  print(f"This number {nbr} is negative.")


#THIS IS ABOUT EXERCISE 17
print("THIS IS ABOUT EXERCISE 17")
print("THIS IS ABOUT CHECKING WHETHER A NUMBER IS EVEN OR ODD")
nbr=float(input("Enter the value:"))
if nbr % 2==0:
  print (f"The inputed number{nbr} is even")
else :
  print(f"The inputed number{nbr} is odd ")


#THIS IS ABOUT EXERCISE 18
print("THIS IS ABOUT EXERCISE 18")
print("THIS IS ABOUT FINDING THE LARGEST NUMBER AMONG THREE NUMBERS")
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
print("===========================================================  ")
if n1>=n2 and n1>=n3:
  print(f"The largest number is {n1}")
elif n2>=n1 and n2>=n3:
  print(f"The largest number is {n2}")
else:
  print(f"The largest number is {n3}")


#THIS IS ABOUT EXERCISE 19
print("THIS IS ABOUT EXERCISE 19")
print("THIS IS ABOUT CHECKING THE GRADE OF A STUDENT BASED ON MARKS")
marks=float(input("Enter marks:"))
if marks>=80:
 print("Grade A")
 print("Excellent keep it up!!!")
elif marks>=70:
 print("Grade B")
 print("Very good next time is 90 and above")
elif marks>=60:
 print("Grade C")
 print("Good but still improve")
elif marks>=50:
 print("Grade D")
 print("Keep working working hard")
elif marks>=0:
 print("Grade E")
 print("Improve your marks")
elif marks<0:
  print("invalid marks")


#THIS IS ABOUT EXERCISE 20
print("THIS IS ABOUT EXERCISE 20")
print("THIS IS ABOUT CHECKING WHETHER A YEAR IS LEAP YEAR OR NOT")
year = int(input("Enter a year: "))
print(".....................................................................")
if year>0 and year % 400 == 0:
    print("Leap year")
elif year>0 and year % 100 == 0:
    print("Not a leap year")
elif year>0 and year % 4 == 0:
    print("Leap year")
elif year<0:
    print("unknown year")
else:
  print("Invalid year")





