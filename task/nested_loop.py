#nested loop

for x in range(5):
    for i in range(5):
        if x == 2 and i == 2:
            print("$",end=" ")
        else:
            print("*",end=" ")
            
    print()
    
print("2")
for x in range(1,6):
    for i in range(1,x+1):
        print("*",end=" ")
    print()


print("pattern 3")
for x in range(1,5):
    for i in range(1,x+1):
        if i % 2 == 0:
            print("0",end=" ")
        else:
            print("1",end=" ")
        
    print()
