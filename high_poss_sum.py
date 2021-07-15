# For given array, cacluate Higest possible sumof 3 elements in a given array
# if size of array less than 4, print Invalid Input

from itertools import combinations


a = list(map(int, input().split()))
if len(a) < 4:
    print('Invalid Input')
else:
    res = 0
    print(list(combinations(a, 3)))
    for i in list(combinations(a, 3)):
        if sum(i) > res:
            res = sum(i)
    print(res)
