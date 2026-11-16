#first way is to declare the max number and index slargest to 
[0] 

numbers = [423, 754, 512, 963, 999, 345, 465, 549, 898, 989]
b=max(numbers)
largest=b
slargest=numbers[0]
for n in numbers:
  if n < largest and n > slargest :
    slargest=n
print("Original list:", numbers)
print("Largest number:", largest)
print("Second largest number:",slargest)




#another way is to index all to zero

print("=======================================================================")

numbers = [423, 754, 512, 963, 999, 345, 465, 549, 898, 989]
largest = numbers[0]
second_largest = numbers[0]
for n in numbers:
   if n > largest:
    largest = n
for n in numbers:
  if n > second_largest and n < largest:
    second_largest = n
print("Original list:", numbers)
print("Largest number:", largest)
print("Second largest number:", second_largest)

print("ANOTHER METHOD TO FIND THE SECOND LARGEST NUMBER IN A LIST")
#use sort
numbers = [423, 754, 512, 963, 999, 345, 465, 549, 898, 989]

sorted_numbers = sorted(numbers)

print("Largest:", sorted_numbers[-1])
print("Second largest:", sorted_numbers[-2])


#to input a number with space
#here we use map to apply to all iterations in list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = sorted(set(numbers))
print("Original list:", numbers)
print("Largest:", sorted_numbers[-1])
print("Second largest:", sorted_numbers[-2])


#create an array
#then sort it 
numbers = []
size = int(input("How many numbers? "))
for i in range(size):
    n = int(input("Enter number: "))
    numbers.append(n)
print("Original list:", numbers)
sorted_numbers = sorted(set(numbers))#i use set to make it good and remove duplicates
print(sorted_numbers)
if len(sorted_numbers) >= 2:
    print("Largest:", sorted_numbers[-1])
    print("Second largest:", sorted_numbers[-2])
else:
    print("You must enter at least two different numbers.")