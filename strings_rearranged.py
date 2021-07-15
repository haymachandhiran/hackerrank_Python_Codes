#https://www.youtube.com/watch?v=h5hRm9CuLIs&list=PL7f0FYY_3hQDS79OekQv5PO7jCDGUaEyk&index=6

#Find no of ways strings can be arranged when vowels are together

#Eg : sister op: 120 ;  animation op: 1800

import math as m
s = 'sister'
vow_count = 0
cons_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in s:
    if i in vowels:
        vow_count += 1
    else:
        cons_count += 1
vow_fact = m.factorial(vow_count)
cons_fact = m.factorial(cons_count+1)
rep_fact = 1
for i in set(s):
    if s.count(i) > 1:
        rep_fact *= m.factorial(s.count(i))
res = int((vow_fact * cons_fact) / rep_fact)
print(vow_fact)
print(cons_fact)
print(rep_fact)
print(res)
