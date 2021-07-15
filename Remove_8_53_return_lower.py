s = 'AB5HJ53JK8LP'
s += ' '
print(s)
print(len(s))
for i in range(len(s)-1):
    if s[i] == '8':
        s = s[:i] + s[i+1:]
    if s[i] == '5':
        if s[i+1] == '3':
            s = s[:i] + s[i + 2:]
print(s.lower())
