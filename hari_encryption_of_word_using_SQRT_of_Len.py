from math import *
from itertools import zip_longest


def encryption(s):
    b = []
    k = ceil(pow(len(s) ,.5))
    for i in range(0, len(s), k):
        b.append(s[i:i+k])
    z = []
    for i in zip_longest(*b, fillvalue=''):
        z.append(i)
    res = []
    for i in range(len(z)):
      res.append(''.join(z[i]))
    return ' '.join(res)

s = 'feedthedog'
print(encryption(s))