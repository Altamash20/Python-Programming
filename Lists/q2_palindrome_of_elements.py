myList = ["r", "a", "c", "e", "c", "a", "r"]
myList2 = [1, 2, 3]

copy_myList = myList.copy()
copy_myList.reverse()
copy_myList2 = myList2.copy()
copy_myList2.reverse()

if(copy_myList == myList):
    print("Palindrome")
else:
    print("NOT Palindrome")


if(copy_myList2 == myList2):
    print("Palindrome")
else:
    print("NOT Palindrome")


