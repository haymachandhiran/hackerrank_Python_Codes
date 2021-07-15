#https://www.hackerrank.com/challenges/funny-string/problem


def funnyString(s):
    r = s[::-1]
    s_ascii_value = []*(len(s) + 1)
    r_ascii_value = []*(len(s) + 1)
    for i in range(len(s)):
        s_ascii_value.append(ord(s[i]))
        r_ascii_value.append(ord(r[i]))

    for i in range(len(s)-1):
        if abs(s_ascii_value[i] - s_ascii_value[i+1]) == abs(r_ascii_value[i] - r_ascii_value[i+1]):
            continue
        else:
            return 'Not Funny'
    return 'Funny'


S = input()
result = funnyString(S)
print(result)
