class A:
    def __init__(self,stu_name):
        self.n = stu_name

    def displayA(self):
        print("Student details :-")
        print("Student name : ",self.n)

class B(A):
    def input(self,stu_age):
        self.a = stu_age

    def displayB(self):
        print("Student age : ",self.a)

class C(B):
    def __init__(self,stu_sub):
        self.s = stu_sub

    def displayC(self):
        print("Student subject : ",self.s)

class D(A):
    def inputd(self,stu_marks):
        self.m = stu_marks

    def displayD(self):
        print("Student marks : ",self.m)

class E(B,D):
    def inpute(self,stu_grd):
        self.g = stu_grd

    def displayE(self):
        print("Student grade : ",self.g)


e1 = E("kajal")
e1.displayA()
e1.input(23)
e1.displayB()
c1 = C("maths")
c1.displayC()
e1.inputd(80)
e1.displayD()
e1.inpute("A")
e1.displayE()

        
