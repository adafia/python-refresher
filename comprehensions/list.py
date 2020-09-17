# Double the numerical value of each element of a list numbers using a regular for loop
numbers = [1, 3, 5]
double = []

for number in numbers:
  double.append(number * 2)


# Double the numerical value of each element of a list numbers using list comprehension
number_list = [1, 3, 5]
double_list = [n * 2 for n in number_list]

# Experimenting with sort and sorted
number_list = [1, 3, 5].sort()
double_list = sorted([n * 2 for n in number_list])


# looping through a list of strings and appending elements that starts with "s" to another list using a regular for loop
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
  if friend.startswith("S"):
    starts_s.append(friend)

print(starts_s)


# looping through a list of strings and appending elements that starts with "s" to another list using list comprehension
friend_list = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s_list = [friend for friend in friend_list if friend.startswith("S")]

print(id(friend_list))
print(id(starts_s_list))