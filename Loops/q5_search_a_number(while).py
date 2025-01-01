x = int(input("Enter the number:"))
my_tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

j = 0
while j<len(my_tup):
    if(x == my_tup[j]):
        print("Found at index",j)
    j+=1
    