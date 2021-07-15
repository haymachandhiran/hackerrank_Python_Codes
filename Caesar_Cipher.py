#https://www.hackerrank.com/challenges/caesar-cipher-1/problem


def caesarCipher(s, n, k):
    res = ''
    for i in range(n):
        temp = 0
        if s[i].islower():
            temp = ord(s[i]) +(k % 26)
            if temp > 122:
                temp = (temp - 122) + 96
                res += chr(temp)
            else:
                res += chr(temp)
        elif s[i].isupper():
            temp = ord(s[i]) + (k % 26)
            if temp > 90:
                temp = ((temp - 90) + 64)
                res += chr(temp)
            else:
                res += chr(temp)
        else:
            res += s[i]
    return res



n = int(input())
s = input()
k = int(input())
print(caesarCipher(s, n, k))
print(ord('A'))
print(ord('Z'))

# print(ord('z')) 122

