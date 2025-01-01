my_tup = (1, 4, 9, 16, 25, 
          36, 49, 64, 81, 100)

x = int(input("Enter number:"))
j = 0
for num in my_tup:
    if num == x:
        print("Number", x, "is found at index", j)
    j+=1