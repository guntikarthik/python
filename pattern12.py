#1  2  3  4  5
#16 17 18 19 6
#15 24 25 20 7
#14 23 22 21 8
#13 12 11 10 9

num=5
n=1  #for counting values from 1 to 25
n_list=[[0 for x in range(num)]for y in range(num)]
low=0
high=num-1
count=int((num+1)/2)
for i in range(count):
    for j in range(low,high+1):
        n_list[i][j]=n
        n=n+1
    for j in range(low+1,high+1):
        n_list[j][high]=n
        n=n+1
    for j in range(high-1,low-1,-1):
        n_list[high][j]=n
        n=n+1
    for j in range(high-1,low,-1):
        n_list[j][low]=n
        n+=1
    low=low+1
    high=high-1
for i in range(num):
    for j in range(num):
        print(n_list[i][j],end="\t")
    print()