#https://www.hackerrank.com/challenges/counting-valleys/problem

def count_val(s):
    temp = 0
    res = 0
    for i in range(len(s)):
        if s[i] == 'D':
            temp -= 1
        else:
            temp += 1
        if temp == 0 and s[i] != 'D':
            res += 1
    return res


S = 'UDDDUDUU'
print(S)
print(count_val(S))
