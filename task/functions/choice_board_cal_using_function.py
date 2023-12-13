def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
def mod(num1,num2):
    return num1 % num2
status = True
while(status):
 print("\t===========Choice Board===========")
 print("\n\t1. Addition")
 print("\t2. Substraction")
 print("\t3. Multiplication")
 print("\t4. Division")
 print("\t5. Modulo")
 print("\t6. Exit")
 ch = int(input("\tEnter Your Choice : "))
 num1 = int(input("\tEnter 1st number : "))
 num2 = int(input("\tEnter 2nd number : "))
 if ch == 1:
   print("\tYour Ans : ",add(num1,num2))
 elif ch == 2:
   print("\tYour Ans : ",sub(num1,num2))
 elif ch == 3:
   print("\tYour Ans : ",mul(num1,num2))
 elif ch == 4:
   print("\tYour Ans : ",div(num1,num2))
 elif ch == 5:
   print("\tYour Ans : ",mod(num1,num2))    
 ch = input("\tDo You Want to continue ? ['y/n'] : ")
 if ch == 'y' or ch == 'Y':
     status = True
 else:
     status = False
     print("\tThank You")
