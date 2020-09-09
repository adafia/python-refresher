def divide(dividend, divisor):
  if divisor != 0:
    return dividend / divisor
  else:
    return "Nope"


result = divide(dividend=15, divisor=3)
print(result)