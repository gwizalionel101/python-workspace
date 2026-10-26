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