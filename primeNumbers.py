lower=int(input("Enter starting num to check"))
upper=int(input("Enter lower num to check"))
for num in range(lower,upper):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=" ")