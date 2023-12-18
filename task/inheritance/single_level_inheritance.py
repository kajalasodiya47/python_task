class A:
      def displayA(self):
          print("method of class A")


class B(A):
      def displayB(self):
          print("Method of class B")

b = B()
b.displayA()
b.displayB()
          
