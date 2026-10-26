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
  
  