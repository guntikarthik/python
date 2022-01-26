#co primes are num which have gcd of both as 1
#e.g 16,25    21,22
def computeGcd(a,b):
    if b==0:
        return a
    else:
        return computeGcd(b,a%b)

num1=16
num2=22
a=computeGcd(num1,num2)
if a==1:
    print(f"{num1} and {num2} are co-primes")
else:
    print(f"{num1} and {num2} are  not co-primes")

