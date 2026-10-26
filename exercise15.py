# 1. ARITHMETIC OPERATORS (+, -, *, /, %, **, //)
print("=== 1. Arithmetic Operators ===")
a = 15
b = 4

print(f"Addition ({a} + {b}):", a + b)
print(f"Subtraction ({a} - {b}):", a - b)
print(f"Multiplication ({a} * {b}):", a * b)
print(f"Division ({a} / {b}):", a / b)
print(f"Modulus/Remainder ({a} % {b}):", a % b)
print(f"Exponent/Power ({a} ** {b}):", a ** b)
print(f"Floor Division ({a} // {b}):", a // b)
print("-" * 30)


# 2. COMPARISON OPERATORS (==, !=, >, <, >=, <=)
print("=== 2. Comparison Operators ===")
x = 10
y = 20

print(f"Is Equal To ({x} == {y}):", x == y)
print(f"Is Not Equal To ({x} != {y}):", x != y)
print(f"Greater Than ({x} > {y}):", x > y)
print(f"Less Than ({x} < {y}):", x < y)
print(f"Greater Than or Equal To ({x} >= {y}):", x >= y)
print(f"Less Than or Equal To ({x} <= {y}):", x <= y)
print("-" * 30)


# 3. LOGICAL OPERATORS (and, or, not)
print("=== 3. Logical Operators ===")
has_id = True
is_adult = False

print(f"AND Logic (Both must be True): {has_id} and {is_adult} =", has_id and is_adult)
print(f"OR Logic (At least one must be True): {has_id} or {is_adult} =", has_id or is_adult)
print(f"NOT Logic (Inverts the value): not {is_adult} =", not is_adult)
print("-" * 30)


# 4. ASSIGNMENT OPERATORS (=, +=, -=, *=, /=)
print("=== 4. Assignment Operators ===")
num = 5
print("Initial Assignment (num = 5):", num)

num += 3  # Equivalent to: num = num + 3
print("Add and Assign (num += 3):", num)

num -= 2  # Equivalent to: num = num - 2
print("Subtract and Assign (num -= 2):", num)

num *= 2  # Equivalent to: num = num * 2
print("Multiply and Assign (num *= 2):", num)

num /= 4  # Equivalent to: num = num / 4
print("Divide and Assign (num /= 4):", num)
print("-" * 30)


# 5. MEMBERSHIP OPERATORS (in, not in)
print("=== 5. Membership Operators ===")
shopping_list = ["apple", "banana", "cherry"]

print("Is 'apple' in the list?", "apple" in shopping_list)
print("Is 'orange' in the list?", "orange" in shopping_list)
print("Is 'orange' NOT in the list?", "orange" not in shopping_list)