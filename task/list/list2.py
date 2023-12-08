'''
insert() - inserts an item at the specified index
append() - add an item to the end of the list
extend() - append elements from another list to the current list

'''

list1 = ["apple","banana","kiwi"]
list1.insert(1,"orange")
print("insert",list1)

list1.append("banana")
print("append",list1)

list2 = [1,2,3]
list1.extend(list2)
print("extend",list1)
