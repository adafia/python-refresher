movies_watched = {"The Matrix", "Green Book", "Her"}

user_movie = input("Enter the name of a movies you've recently wathed: ")

if user_movie in movies_watched:
  print(f"I've watched {user_movie} too!")
else:
  print("I haven't watched that yet.")
