'''
  a1 = A(12,4)
  a2 = A(23,5)

  check both objects having identical values or not ?
  return True if yes
  else return False
  
'''

class A:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __eq__(self, y):
        return self.value1 == y.value1 and self.value2 == y.value2
    
a1 = A(12, 4)
a2 = A(23, 5)

if a1 == a2:
    print("True")
else:
    print("False")


