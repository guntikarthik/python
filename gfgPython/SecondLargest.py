''' def secondLargest(l):
    temp=[]
    max1=max(l)
    l.remove(max1)
    max2=max(l)
    return max2 '''
from re import X


def secondLargest(l):
    if len(l)<=1:
        return None
    lar=l[0]
    sLar=None
    for x in l[1:]:
        if x>lar:
            slar=lar
            lar=x
        elif x!=lar:
            if slar==None or slar<x:
                slar=x
    return slar



l=[10,20,30,40,50,60]
print(secondLargest(l))