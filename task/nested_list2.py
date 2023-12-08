l1 = [12,3.434,45,"Hello",74,34.54,"Happy",'alpha']
strs=[]
ints=[]
floats=[]

for element in l1:
    if isinstance(element,int):
        ints.append(element)
    elif isinstance(element,float):
        floats.append(element)
    elif isinstance(element,str):
        strs.append(element)
print(ints)
print(floats)
print(strs)
    
