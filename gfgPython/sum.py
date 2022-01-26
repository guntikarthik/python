import re
from wsgiref.handlers import read_environ


'''def sum(n):
    res=0
    for i in range(1,n+1):
        res+=i
    return res
'''
#method2
# using direct formula
def fun2(n):
    return n*(n+1)//2  

num=int(input("Enter number until which you want to add numbers from 0"))
print(fun2(num))

