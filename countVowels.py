# count vowels in given sentence
''' s="Tom and Jerry is best anime"   #8 vowels
count=0
for i in s.lower():
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count+=1
print(count) '''

sentence="WELcome EVerYonE"  #7
count=0
l1=["a","e","i","o","u"]
for char in sentence.lower():
    if char in l1:
        count+=1
print(count)