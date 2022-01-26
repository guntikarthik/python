#return index of pattern at every instance in string
#e.g : "geeks for geeks"  search "geeks" o/p   0 11
# e.g  "AAAAA"  find "aaa"  o/p : 0 1 2     
txt=input("Enter text: ")
pat=input("Enter pattern to seach in string")
pos=txt.find(pat)
while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1)