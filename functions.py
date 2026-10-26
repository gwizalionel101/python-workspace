def me(*params):
  return sum(params)
print(me(1,2,3,4,5))

def them(*params):
  return params[0] - sum(params[1:])
print(them(100,50,20))