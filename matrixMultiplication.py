#rows in m1 == col in m2 for matrix multiplication
p=int(input("Enter no. of rows in matrix 1"))
q=int(input("Enter no. of columns in matrix 2"))
r =int(input("Enter no. of rows in matrix 2 or col in m1"))
print("Enter elements  in matrix1")
m1=[[int(input()) for i in range(r)] for j in range(p)]
print("matrix1")
for i in range(p):
    for j in range(r):
        print(format(m1[i][j],"<3"),end=" ")
    print()
m2=[[int(input()) for i in range(q)] for j in range(r)]
print("matrix2")
for i in range(r):
    for j in range(1):
        print(format(m2[i][j],"<3"),end=" ")
    print()
res=[[0 for i in range(q)] for i in range(p)]
for i in range(p):
    for j in range(q):
        for k in range(r):
            res[i][j]=res[i][j]+m1[i][k]*m2[k][k]
for i in range(p):
    for j in range(q):
        print(format(res[i][j],"<3"))
    print()
