class A:
    def __init__(self,stu_name):
        self.n = stu_name
        
    def displayS(self):
        print("Student details :- ")
        print("Student name : ",self.n)
        
class B(A):
     def input(self,stu_age):
         self.a = stu_age
         
     def displaySt(self):
        print("student age : ",self.a)

class C(A):
      def displayC(self):
          print("End")

b1 = B("kajal")
b1.displayS()
b1.input(20)
b1.displaySt()
c1 = C("neha")
c1.displayS()
c1.displayC()
