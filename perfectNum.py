#perfect num is num which is same as sum of its factors starting from 1 to n excluding itself
# 6 is perfect number 
#  sum of factors exluding 6 is 1+2+3=6
num=int(input("Enter num to find whether perfect or not"))
sum=0
for i in range(1,num): #excluding num and considering all other factors 
    if num%i==0:   #if factors gets remainder zero add to sum
        sum+=i
if sum==num:
    print(f"{num} is perfect number" )
else:
     print(f"{num} is not perfect number" )
