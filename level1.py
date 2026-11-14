#THIS IS EXERCISE 1
print("THIS IS ABOUT EXERCISE 1")
name="GWIZA MUCYO LIONEL"
School="RWANDA CODING ACADEMY"
welcome_message="Welcome at our school "
print(name+"\n"+School+"\n"+welcome_message)

#THIS IS EXERCISE 2
print("THIS IS ABOUT EXERCISE 2")
fn=input("Enter your full name:")
country=input("Enter your nationality:")
age=input("Enter your age:")
print(f"my full names are {fn},I am a {country} and I am aged {age}.")

#THIS IS EXERCISE 3
print("THIS IS ABOUT EXERCISE 3")
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


  #THIS IS EXERCISE 4
  print("THIS IS ABOUT EXERCISE 4")
  print("Which conversion do you want?\n1.from Celcius to Fahrenheit(C ---> F)\n2.from Fahnrenheit to Celcius(F ---> C)") 
print("..................................................................................")
option=int(input("Enter your option:"))
if option == 1:
  cel=float(input("Enter your temperature in Celcius:"))
  print("your temperature in fahrenheit is:",cel*1.8+32)
elif option == 2:
  temp=float(input("Enter your temperature in Fahrenheit:"))
  print("your temperature in Celcius is:",(temp-32)*0.5556)
else :
  print("invalid option")

#THIS IS ABOUT EXERCISE 5
print("THIS IS ABOUT EXERCISE 5")
print("========== I AM HERE TO CALCULATE THE AREA AND PERIMETER OF YOUR RECTANGLE ==========")
length=float(input("Rectangle's length: "))
width=float(input("Rectangle's width:"))
print(f"What do you want to calculate?\n1.The Perimeter\n2.The Area")
while True:
 choice=int(input("What's your choice:"))
 print(".............................................................................")
 if choice == 1 :
  print("The Perimeter of this rectangle is:",(length+width)*2)
  break
 elif choice == 2 :
  print("The Area of this rectangle is:",length*width)
  break
 else:
  print("Invalid choice")
   
 #THIS IS ABOUT EXERCISE 6
 print("THIS IS ABOUT EXERCISE 6")
 print("THIS IS ABOUT EXCHANGING TWO NUMBERS")
 a = float(input("a:"))
b = float(input("b:"))
a, b = b, a
print("a =", a)
print("b =", b)

#THIS IS ABOUT EXERCISE 7
print("THIS IS ABOUT EXERCISE 7")
print("THIS IS ABOUT DATA TYPES")
value1 = int(input("Enter an integer: "))
value2 = float(input("Enter a decimal number: "))
value3 = input("Enter True or False: ") == "True"
value4 = input("Enter some text: ")
value5 = input("Enter list items separated by commas and in []: ").split(",")
value6 = input("Enter a dictionary key: ")
value7 = input("Enter its value: ")
my_dict = {value6: value7}
print(type(value1))
print(type(value2))
print(type(value3))
print(type(value4))
print(type(value5))
print(type(my_dict))

#THIS ABOUT EXERCISE 8
print("THIS IS ABOUT EXERCISE 8")
print("=== SECONDS CONVERTER ===")
total_seconds = int(input("Enter the total number of seconds: "))
years = total_seconds // 31536000
remaining_seconds = total_seconds % 31536000
months = remaining_seconds // 2592000
remaining_seconds = remaining_seconds % 2592000
days = remaining_seconds // 86400
remaining_seconds = remaining_seconds % 86400
hours = remaining_seconds // 3600
remaining_seconds = remaining_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print("----------------------------------------------------")
print("Years:", years)
print("Months:", months)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

#THIS ABOUT EXERCISE 9
print("THIS IS ABOUT EXERCISE 9")
print("===THE SIMPLE INTEREST CALCULATOR===")
p=float(input("Enter the principal:"))
t=float(input("Enter the time in years:"))
r=float(input("Enter the rate:"))
I=(p*r*t)/100
print(".....................................................")
print("=>The simple interest is :",I)
print(f"=>the new amount is :",p+I)
 

#THIS ABOUT EXERCISE 10
print("THIS IS ABOUT EXERCISE 10")
print("..........THE BMI CALCULATOR..........")
kg=float(input("Input your weight in kg:"))
h=float(input("Input your height in meteres(m):"))
bmi=kg/(h**2)
print("==============================================")
print(f"Your BMI is:",bmi)
if bmi>=30.0:
  print("You have Obesity")
elif bmi<=29.9 and bmi>24.9:
  print("You are Overweight")
elif bmi<=24.9 and bmi>18.5:
  print("You have Normal Weight")
elif bmi<18.5:
  print("You are underweight")
