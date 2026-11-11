rows = int(input("Enter the number of rows: "))  #taking input from user
for i in range(1,rows+1):
  print(" "*(rows-i) + "*"*(2*i-1))  #here i is the current row number and remember that the last number in range dont count it
for i in range(rows-1,0,-1):
  print(" "*(rows-i) + "*"*(2*i-1))  #here i is the current row number and we are reversing the upper case