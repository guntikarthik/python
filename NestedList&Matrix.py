num=3
#print nested list using list comprehension of value 0
nested_list= [[0 for i in range(num)]for i in range(num)]
print(nested_list)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#to print in matrix form
for i in range(num):
    for j in range(num):
        print(nested_list[i][j],end="\t")
    print()
 #0       0       0
 #0       0       0
 #0       0       0