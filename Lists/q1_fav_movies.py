mov1 = input("Enter your first favourite movie: ")
mov2 = input("Enter your second favourite movie: ")
mov3 = input("Enter your third favourite movie: ")

myList = [mov1, mov2, mov3]
print(myList)


# alternative way 1

movies = []
movie1 = input("Enter your first fav movie:")
movie2 = input("Enter your second fav movie:")
movie3 = input("Enter your third fav movie:")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


# alternative way2

movies = []
movies.append(input("Enter your first fav movie: "))
movies.append(input("Enter your second fav movie: "))
movies.append(input("Enter your third fav movie: "))
print(movies)

