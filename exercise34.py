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