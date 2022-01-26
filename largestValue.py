def maxValue(l):
    if not l:
        return None
    else:
        res=l[0]
        for i in l:
            if i>res:
                res=i
        return res
l=[10,20,30,40]
print(maxValue(l))