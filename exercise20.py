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
