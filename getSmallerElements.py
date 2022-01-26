# get smaller elements of list than given x value
l=[8,100,20,40,3,7]
x=10
print([i for i in l if i<x])
l2=[100,20,40,60,80,2]
y=60
temp=[]
for i in l2:
    if i<y:
        temp.append(i)
print(temp)
