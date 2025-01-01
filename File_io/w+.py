f = open("demo3_file.txt", "w+")
print(f.read())
f.close()

f.write("I will learn Java.")
f.close()
f = open("demo3_file.txt", "r")

print(f.read())
f.close()
