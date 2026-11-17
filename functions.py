def me(*params):
  return sum(params)
print(me(1,2,3,4,5))

def them(*params):
  return params[0] - sum(params[1:])
print(them(100,50,20))

#you can create functions without def keyword
#eg
greet = lambda:print("hello; world!")
greet()


def my_function(greeting,*names):
    for name in names:
        print(greeting, name)
my_function("Hello", "Emil", "Tobias", "Linus")
#itis not possible to write (*names, greeting) it outputs an error
#except my_function("Emil", "Tobias", "Linus", greeting="Hello")
