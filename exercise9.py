print("===THE SIMPLE INTEREST CALCULATOR===")
p=float(input("Enter the principal:"))
t=float(input("Enter the time in years:"))
r=float(input("Enter the rate:"))
I=(p*r*t)/100
print(".....................................................")
print("=>The simple interest is :",I)
print(f"=>the new amount is :",p+I)
 
