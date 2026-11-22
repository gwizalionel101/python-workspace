import calendar
import pyfiglet
print(pyfiglet.figlet_format("2027", font="block"))
print("        THE YEAR OF NEW BEGINNINGS")
year = int(input("Enter a year: "))
for m in range(1, 13):
    print("\n", "✨", calendar.month_name[m].upper(), "✨")
    print(calendar.month(year, m))
print("             ✨ MAKE EVERY DAY COUNT ✨")




#or 
yr=int(input("Enter the year to print:"))
print(calendar.calendar(year, 2, 1, 8, 3))
#these numbers controls:
#2:width of each date column(2 characters)
#1:number of lines used for each week
#8:number of spaces between month column
#3:number of months displayed per row 