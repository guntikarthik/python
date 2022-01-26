def palindromicPrime(n):
    for i in range(1,n):
        if i%n==0:
            print("not palindromic prime")
            break
        else:
            return palindrome(i)
def palindrome(i):
    a=str(i)
    b=a[::-1]
    if a==b:
        print("palindromic prime")
    else:
        print("not palindromic prime")




palindromicPrime(124)