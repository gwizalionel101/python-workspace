numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = []
for n in numbers:
    if n not in unique_numbers:
        unique_numbers.append(n)
print("Original list:", numbers)
print("List without duplicates:", unique_numbers)