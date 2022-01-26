# anagram string is another string which has same no.of char and only seiquence is diff
#e.g earth and heart, abc & bac  are anagrams
str1="earth"
str2="hearts"
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)
if len(str1)==len(str2):
    if sorted_str1==sorted_str2:
        print(f"{str1} and {str2} are anagrams")
    else:
        print(f"{str1} and {str2} are  not anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")