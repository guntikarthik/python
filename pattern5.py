#1
#2 3
#4 5 6 
#7 8 9 10
n=4
c=1
for i in range(n+1):
    for j in range(i):
        print(c,end=" ")
        c+=1
    print()