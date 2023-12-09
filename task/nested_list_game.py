'''
  l1 = [12,45,343,545,5,6,4,7]


  lucky : 5

  computer = [12,45,343,545]
  user = [5,6,4,7]

  round : 1
  user win
  u_score = 1
  c_score = 0

'''

import random
l1 = [12,45,343,545,5,6,4,7]
computer = [12,45,343,545]
user = [5,6,4,7]
i = 1
while i < 5:
 x = random.choice(l1)
 print("lucky : ",x)
 if(x in computer):
    computer.remove(x)
    print(computer)
    print("round : ",i)
    print("computer win")
    print("c_score = ",i)
    if computer == []:
       break
 elif(x in user):
    user.remove(x)
    print(user)
    print("round : ",i)
    print("user win")
    print("u_score = ",i)
    if user == []:
        break    
    i += 1

