from operator import length_hint

movies = ["SAW", "John Carter", "Edge of tomorrow", "Merry Poppins"]
movies.append("Fellowship of the ring")

print("Movies in the list:")
for movie in movies:
    print(movie)


movies=["SAW", "John Carter", "Edge of Tomorrow", "Merry Poppins", "Fellowship of the ring"]
print("Find out the movie name: ")
print(movies[0])


movies=["SAW", "John Carter", "Edge of Tomorrow", "Merry Poppins", "Fellowship of the ring"]
movies.insert(0,"The two towers")
print("Find out the movie name: ")
print(movies[0])


movies=["SAW", "John Carter", "Edge of Tomorrow", "Merry Poppins", "Fellowship of the ring"]
movies.insert(0,"The two towers")
print("Find out the movie index: ")
index = movies.index("Fellowship of the ring")
print("The movie Fellowship of the ring has index : ", index)


movies=["SAW", "John Carter", "Edge of Tomorrow", "Merry Poppins", "Fellowship of the ring"]
length = len(movies)
print("The length of the list is : ", length)


movies=["SAW", "John Carter", "Edge of Tomorrow", "Merry Poppins", "Fellowship of the ring"]
movies.reverse()
print("Reversed movie list: ", movies)


movies=["SAW", "John Carter", "Edge of Tomorrow", "Merry Poppins", "Fellowship of the ring"]
movies.sort()
print("Reversed movie list: ", movies)





