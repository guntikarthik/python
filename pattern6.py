#get string from user and print in right triangle form
n="python"
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end="")
    print()