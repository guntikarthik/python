s="Devilliars"
#reverse string in single line
#print(s[::-1])

#reverse using for loop
reversed_string=""  # we take empty string and concatenate char every time in loop
for i in s:
    reversed_string=i+reversed_string
print(reversed_string)
