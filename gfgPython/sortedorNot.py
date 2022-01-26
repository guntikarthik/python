def sortedList(l):
    a=l[0]
    for i in l[1:]:
        if i>=a:  # compare current value with previous value each time 
            a=i
        else:
            return False
    return True

l=[1,2,3]
print(sortedList(l))