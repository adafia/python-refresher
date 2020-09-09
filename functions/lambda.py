def double(x):
  return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]

doubled_ = map(double, sequence)
doubled_ = list(map(lambda x: x * 2, sequence))