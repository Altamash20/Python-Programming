f = open("demo_file.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()


f = open("demo_file.txt", "r")
data1 = f.read(10)
print(data1)
print(type(data1))
f.close()


f = open("demo_file.txt", "r")
line1 = f.readline()
print(line1)
print(type(line1))


line2 = f.readline()
print(line2)
print(type(line2))


line3 = f.readline()
print(line3)
print(type(line3))

