
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
a=len(matrix1)
b=len(matrix1[0])
res=[[0 for i in j] for j in matrix1]
for i in range(a):
    for j in range(b):
        res[i][j]=matrix1[j][i]
print(res) 