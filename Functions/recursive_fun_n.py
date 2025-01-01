def display(n):
    if(n==0):
        return 0
    print(n)
    display(n-1)

display(8)