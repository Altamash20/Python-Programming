dict_nest = {
    "men1":{
        "name" : "john",
        "age" : 36
    },
    "men2":{
        "name" : "george",
        "age" : 28
    },
    "men3": [{"name":"jack"}, {"age":31}]
}

print(dict_nest)
print(dict_nest["men2"]["name"])
print(dict_nest["men3"][1]["age"])