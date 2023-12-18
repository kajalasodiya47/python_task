class A:
      def displayA(self):
          print("method of class A")


class B(A):
      def displayB(self):
          print("Method of class B")

class C(B):
      def displayC(self):
          print("method of class C")

c = C()
c.displayA()
c.displayB()
c.displayC()
          
