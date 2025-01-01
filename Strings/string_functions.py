str = "I loves coding. I am a passionate problem solver."
print(str.endswith("lver."))
print(str.endswith("r."))
print(str.endswith("coding."))
print(str.endswith("apple."))
print(str.endswith("."))


str1 = "hi i am altamash!"
print(str1.capitalize())
print(str1)

str2 = "hi i am altamash!"
str3 = str2.capitalize()
print(str3)

str4 = "I loves coding. I am a passionate problem solver."
print(str4.replace("o", "i"))
print(str4.replace("passionate", "experienced"))
print(str4.replace("ion", "al"))

str5 = "I loves coding. I am a passionate problem solver. I am currently engaged in problem solving."
print(str5.find("problem"))
print(str5.find("coding"))
print(str5.find("elephant"))  # returns -1 if failure. -1 is not that index in case of slicing

str6 = "I loves coding. I am a passionate problem solver. I am currently engaged in problem solving."
print(str6.count(" "))
print(str6.count(" problem"))
print(str6.count("problem"))
print(str6.count("roblem"))
print(str6.count("a"))
print(str6.count("."))
print(str6.count("dolphin"))

