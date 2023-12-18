'''
  que : Sun rise from ?
  ans : east

  queset = {'q1':{'q':"Sun rise from ?",'a':"east"}}

'''
queset = {}

for i in range(1, 11):
    question = input(f'Enter question {i} : ')
    answer = input(f'Enter answer {i} : ')
    queset[f'q{i}'] = {'q': question, 'a': answer}

# Print the nested dictionary
print(queset)



