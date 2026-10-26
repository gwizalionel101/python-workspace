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
