class A:
    def __init__(self,stu_name,stu_age):
        self.n = stu_name
        self.a = stu_age

    def displayS(self):
        print("Student details :- ")
        print("Student name : ",self.n)
        print("student age : ",self.a)

class B(A):
     def input(self,stu_sub,stu_mark):
         self.s = stu_sub
         self.m = stu_mark

     def displaySt(self):
        print("Student name : ",self.s)
        print("student age : ",self.m)

class C(B):
      def displayC(self):
          print("End")

c1 = C("kajal",22)
c1.displayS()
c1.input("maths",80)
c1.displaySt()
c1.displayC()
