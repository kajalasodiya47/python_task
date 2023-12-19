my_dict = {
    "name" : "kajal",
    "sirname" : "asodiya"
    }
print(my_dict)
print(my_dict['name'])

# changeable
my_dict['name'] = "kajalll"
print(my_dict)


my_dict["name1"] = "kajalll"
print(my_dict)

#Duplicates Not Allowed .Dictionaries cannot have two items with the same key
my_dict["name2"] = "kajalll"
print(my_dict)

print(len(my_dict))

my_dict1 = {
   "name" : "kajal",
   "age" : 22,
   "boolean" : False,
   "hobby" : ["music","reading","travelling"]
    }
print(my_dict1)
print(type(my_dict1))
print(my_dict1['hobby'][0])

my_dict2 = dict()
print(type(my_dict2))
