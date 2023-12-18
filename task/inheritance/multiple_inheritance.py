class A:
      def displayA(self):
          print("method of class A")

class B(A):
      def displayB(self):
          print("method of class B")

class C(A):
      def displayC(self):
          print("method of class C")
          
class D(B,C):
      def displayD(self):
          print("method of class D")

d1 = D()
d1.displayA()
d1.displayB()
d1.displayC()
d1.displayD()
