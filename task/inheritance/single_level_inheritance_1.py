class A:
    def __init__(self,x,y):
        self.n1=x
        self.n2=y

    def displayA(self):
        print("number 1 is : ",self.n1,"and number 2 is : ",self.n2)


class B(A):
    def displayB(self):
        print("Hello from child class")

b1 = B(14,24)
b1.displayA()
b1.displayB()
