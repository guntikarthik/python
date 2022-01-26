#DIRECT METHODS
#method1 using list slicing
'''l=[10,20,30,40,50]
d=3
print(l[d:]+l[:d])'''
#method2 using deque
from collections import deque
l=[10,20,30,40,50]
d=3
de=deque(l)  #convert list to deque type
de.rotate(-d)
l=list(de)
print(l)

