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
   
 