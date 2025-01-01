with open("demo7_file.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)



with open("demo7_file.txt", "w") as f:
    f.write(new_data)