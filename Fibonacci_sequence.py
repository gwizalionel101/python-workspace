print("This is Fibonacci sequence")
numbers = [0, 1]
num = [0, 1]
for i in range(9):
    nf = numbers[-1] + numbers[-2]
    numbers.append(nf)
    num.append(nf)
print(num)


#another way
a = 0
b = 1
num = []
for i in range(10):
    num.append(a)
    c = a + b
    a = b
    b = c
print(num)