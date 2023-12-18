# difference between tuple and list

l1=[12,23,34,54]
t1=(12,34,5,45,65)

print("prev loc List : ",id(l1))
print("pre loc tup : ",id(t1))

l1[2]='hello'
print(l1[2])

t1=(12,34,'hello',45,65)
print(t1[2])


print("new loc List : ",id(l1))
print("new loc tup : ",id(t1))

l1=[12,23,34,54,"kk"]
print(l1[4])
print("new loc List : ",id(l1))

t1=(12,34,5,45,65)
t1[5]="hello"
print(t1[5])
print("pre loc tup : ",id(t1))
