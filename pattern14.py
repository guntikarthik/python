#   1
#  212
# 32123
#4321234

#3parts here 1st spaces from line 1 to 3, 2nd from line1 to line4 , 3rd from line 2 to 4

num=4   #no.of rows are taken from user
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
    print()
