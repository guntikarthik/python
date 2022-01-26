#GCD is same as finding HCF of 2 numbers
#method1: using in-built function gcd
'''import math as m
print(m.gcd(48,64))  #o/p is 16   '''
#method2:using recursive method
def computeGCD(a,b):
    if b==0:
        return a
    return computeGCD(b,a%b)   #a=b and b=a%b
print(computeGCD(4,14))     