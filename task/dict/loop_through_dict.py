my_dict = {
  "name" : "kajal",
  "age" : 19,
  "subject" : "maths"
    }


for i in my_dict:
    print(i)  # print all the keys

for i in my_dict:
    print(my_dict[i])  # print all the values

for i in my_dict.values():
    print(i)          # print all the values using values() method


for i in my_dict.keys():
    print(i)          # print all the keys using keys() method

for i,j in my_dict.items():
    print(i,j)
