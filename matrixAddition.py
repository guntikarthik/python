# for matrix addition we should check whether rows and columns are equal to both matrices
#get no.of rows and columns from user
rows=int(input("Enter no.of rows you want "))
col=int(input("Enter no. of col you want"))
print("Enter matrix1 elements")
matrix1=[[int(input()) for i in range(col)]for j in range(rows)]
print("matrix1 is:")
for i in range(rows):
    for j in range(col):
        print(format(matrix1[i][j],"<3"),end=" ")
    print()
print("Enter matrix2 elements")
matrix2=[[int(input()) for i in range(col)]for j in range(rows)]
print("matrix2 is:")
for i in range(rows):
    for j in range(col):
        print(format(matrix2[i][j],"<3"),end=" ")
    print()
res=[[0 for i in range(col)]for j in range(rows)]
print("addition of matrix1 and matrix2 is:")
for i in range(rows):
    for j in range(col):
        res[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(rows):
    for j in range(col):
        print(format(res[i][j],"<3"),end=" ")
    print()     
