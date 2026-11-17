numbers = [2, 4, 6, 8]

result = map(lambda x: x * 2, numbers)

print(list(result))
#result is [4,8,12,16]

x = range(3, 10)

result = map(str, x)

print(list(result))
#result is ['3', '4', '5', '6', '7', '8', '9']

#map should always have this structure
#map(function, iteration)