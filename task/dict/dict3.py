my_dict = dict(name="kajal",sirname="asodiya")
print(type(my_dict))
print(my_dict)
print(my_dict['name'])

print(my_dict.get('sirname'))

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# update method
my_dict.update({"name":"kajall"})
print(my_dict)

my_dict.popitem()
print(my_dict)
