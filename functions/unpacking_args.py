def multiply(*args):
  print(args)
  total = 1
  for arg in args:
    total = total * arg

  return total


print(multiply(1, 3, 5))

print("---------add---------")

def add(x, y):
  return x + y

nums = [3, 5]
print(add(*nums))

print("---------add - 2---------")

def add_(x, y):
  return x + y

nums_ = { "x": 15, "y": 25 }
print(add(x=nums_["x"], y=nums_["y"]))
print(add(**nums_))