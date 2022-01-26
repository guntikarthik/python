#we are given list which contains one odd occurance number we should find it
''' def oddOccurance(l):
    for i in l:
        count=l.count(i)
        if count%2!=0:
            res=i
            break
    return res '''
#using bitwise xor
from re import X


def oddOccurance(l):
    res=0
    for x in l:
        res=res^x
    return res
l=[10,30,30,10,30,30,20]  #o/p: 20
print(oddOccurance(l))
