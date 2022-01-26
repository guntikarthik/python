
#1  2  3  4  5
#16 17 18 19 6
#15 24 25 20 7
#14 23 22 21 8
#13 12 11 10 9
num=5
nList=[[0 for x in range(num)]for y in range(num)]
low=0
high=num-1
n=1
count=int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        nList[i][j]=n
        n+=1
    for j in range(low+1,high+1):
        nList[j][high]=n
        n+=1
    for j in range(high-1,low-1,-1):
        nList[high][j]=n
        n+=1
    for j in range(high-1,low,-1):
        nList[j][low]=n
        n+=1
    low+=1
    high-=1   
        

for i in range(num):
    for j in range(num):
        print(nList[i][j],end="\t")
    print()