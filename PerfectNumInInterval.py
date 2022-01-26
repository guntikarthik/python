#6,28 are only perfect num from 1 to 100


lower=int(input("Enter lower limit"))
upper=int(input("Enter upper limit"))
for num in range(lower,upper+1):    #finding num
    sum=0  # sum of factors
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        print(num,end=" ")


