def named(**kwargs):
  print(kwargs)


named(name="Bob", age=25)


def named_(name, age):
  print(name, age)

details = {"name":"Bob", "age":25}
named_(**details)


def print_nicely(**kwargs):
  named(**kwargs)

  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_nicely(name="Bob", age=25)