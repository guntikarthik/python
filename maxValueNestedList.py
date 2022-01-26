#find max value in nested list
def computeMax(l):
    temp=[]
    for i in l:
        if type(i)==list:
            computeMax(i)
        else:
            temp.append(i)
    return max(temp)
l=[7,9,[12,5,[30,15],17],7]
print(computeMax(l))