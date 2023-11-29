print("pattern 1:")

for x in range(5):
   for i in range(5):
       if x == i:
          print("$",end=" ")
       else:  
          print("*",end=" ")
   print()

print("pattern 2:")

for x in range(5):
    for i in range(x):
        print("*",end=" ")
    print()

print("pattern 3:")
    
for x in range(5):
    for i in range(x):
        if i % 2 == 0:
          print("1",end=" ")
        else:
          print("0",end=" ")  
    print()

print("pattern 4:")

k = 1
for x in range(5):
    for i in range(x):
       print(k,end=" ")
       k = k + 1
    print()

print("pattern 5:")
a = 65
for x in range(6):
    for i in range(x):
        print(chr(a),end=" ")
        a = a + 1
    print()

print("pattern 6:")
for x in range(6):
    a = 65
    for i in range(x):
        print(chr(a),end=" ")
        a = a + 1
    print()

print("pattern 7:")
for x in range(1,6):
    print(' '*(5-x)+"*"*x)

print("pattern 8:")
for x in range(5,0,-1):
    print("* "*x)

print("pattern 9:")
for x in range(1,6):
    print(' '*(5-x)+"* "*x)

print("pattern 10:")    
for x in range(5,0,-1):
    print(' '*(5-x)+"* "*x)    
