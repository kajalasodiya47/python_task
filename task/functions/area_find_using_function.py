def circle():
    radius = int(input("\tEnter radius : "))
    area = 3.14 * radius * radius
    print("\tArea of circle : ",area)
def triangle():
    h = int(input("\tEnter height : "))
    b = int(input("\tEnter base : "))
    area = 0.5 * h * b
    print("\tArea of triangle : ",area)
def rectangle():
    l = int(input("\tEnter length : "))
    w = int(input("\tEnter height : "))
    area = l * w
    print("\tArea of rectangle : ",area)
status =True
while(status):
 print("\t=============Area Finder===============")
 print("\t1. Circle")
 print("\t2. Triangle")
 print("\t3. Rectangle")
 ch = int(input("\tEnter choice : "))
 if ch == 1:
   circle()
 elif ch == 2:
   triangle()
 elif ch == 3:
   rectangle()
 c = input("\tDo you want to continue again ? ['y/n'] : ")
 if c == 'y' or c == 'Y':
   status = True
 else:
   status = False
   print("\t9araaafThank you")
