# find co primes in range of numbers when compared with given num
from math import gcd
num=int(input("Enter num "))
lower=int(input("Enter lower limit"))
upper=int(input("Enter uppe limit"))
for i in range(lower, upper+1):
    if gcd(num,i)==1:
        print(i)