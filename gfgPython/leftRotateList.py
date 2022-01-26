from re import X


def leftRotate(l):
    x=l[0]
    len1=len(l)
    for i in range(1,len1):
        l[i-1]=l[i]
    l[len1-1]=x
    return l

l=[10,20,30,40,50]
print(leftRotate(l))