# s1 = 'contact'
# s2 = 'convert'
# replace_count = 0
# for i in range(len(s2)):
#     if s2[i] == s1[i]:
#         pass
#     else:
#         replace_count += 1
#

s1 = 'tenter'
s2 = 'rental'
l1, l2 = len(s1), len(s2)
c = 0
for i in s1:
    if i in s2:
        x = s2.find(i)
        s2 = s2[:x] + s2[x+1:]
        print(s2)
        c += 1
print(max(l1, l2) - c)
