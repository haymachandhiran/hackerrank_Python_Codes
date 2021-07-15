#Take 2 strings and find the common char in two str
#print the common char in ass and des order

str1 = input()
str2 = input()
res = ''
for i in str1:
    if i in str2:
        res += i
        str2 = str2.replace(i, '')
print(sorted(res))
print(sorted(res, reverse=True))

