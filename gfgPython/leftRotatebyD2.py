def rotatedList(l,d):
    a=[]
    len1=len(l)
    for i in range(d):
        a.append(i)
    for i in range(d,len1):
        l[i-1]=l[i]
    return l


l=[10,20,30,40,50]
d=2
print(rotatedList(l,d))