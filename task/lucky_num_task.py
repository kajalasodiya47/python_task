'''
lucky_num = 23


status=True
while status:
  num = int(input("Guess the num : "))
  if num > lucky_num:
     print("Hint : think lesser num")
  elif num < lucky_num:
     print("Hint : think larger num")
  elif num == lucky_num:
     print("Guess right number")
     status=False
'''  
  
lucky_num = 45
status=True
while(status):
  i = 1
  for x in range(1,6):
    num = int(input("Guess the num : "))
    if num > lucky_num:
       print("Hint : think lesser num")
    elif num < lucky_num:
       print("Hint : think larger num")
    elif num == lucky_num:
       print("Guess right number")
       break
       status = False
  ch = input("again?['Y/N']")
  if ch == 'Y' or ch == 'y':
     status = True
  else:
     status = False
