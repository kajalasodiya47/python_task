'''blank list'''

mylist = list()
mylist1 = []
print(type(mylist1))


mylist3 = ["apple","banana","apple",1,2.3,True]
print(mylist3)
print(len(mylist3))
print(mylist3[2:5])
print("Negative indexes : ",mylist3[-4:-1])
mylist3[0:2] = ["orange","kiwi"]
print("change list items with specific range : ",mylist3)

mylist4 = list((1,2,"hello"))
print(mylist4)
print(mylist4[0])
mylist4[1] = 3
print("change:",mylist4)

'''
# characterictics
ordered
changeble
allow duplicates
list can contain different data types

'''

mylist5 = ["kiwi","orange",1,3.4,False]
if "kiwi" in mylist5:
    print("Exists")
