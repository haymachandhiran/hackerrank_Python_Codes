#https://www.hackerrank.com/challenges/closest-numbers/problem

import math
def close_num(arr):
    arr.sort()
    print(arr)
    temp = []
    t = float('inf')
    for i in range(0, len(arr) - 1):
       # print(abs(arr[i] - arr[i+1]))
        if abs(arr[i] - arr[i+1]) < t:
            t = abs(arr[i] - arr[i+1])
            temp.clear()
            temp.append(arr[i])
            temp.append(arr[i+1])
           # print(temp)
        elif abs(arr[i] - arr[i+1]) == t:
            temp.append(arr[i])
            temp.append(arr[i+1])
          #  print(temp)
    temp = list(map(str, temp))
    return ' '.join(temp)


N = int(input().rstrip())
ARR = list(map(int, input().split()))
print(close_num(ARR))
