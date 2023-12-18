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
        print("Student subject : ",self.s)
        print("student mark : ",self.m)

class C(A):
     def inputg(self,stu_grade):
         self.g = stu_grade
         
     def displaySg(self):
        print("Student grade : ",self.g)
                
class D(B,C):
      def displayD(self):
          print("End")

d1 = D("kajal",22)
d1.displayS()
d1.input("maths",80)
d1.displaySt()
d1.inputg("A")
d1.displaySg()
d1.displayD()

