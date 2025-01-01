# def check_for_word():
#     word = "learning"
#     with open("demo8_file.txt", "r") as f:
#         data = f.read()
#     if(word in data):
#         print("Found")
#     else:
#         print("Not found")

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("demo9_file.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
           

print(check_for_line())