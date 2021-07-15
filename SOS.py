# https://www.hackerrank.com/challenges/mars-exploration/problem


def marsExploration(s):
    l = len(s)
    sos_count = 0
    for i in range(0, l, 3):
        if s[i] != 'S':
            sos_count += 1
        if s[i + 1] != 'O':
            sos_count += 1
        if s[i + 2] != 'S':
            sos_count += 1
    return sos_count


s = input()
result = marsExploration(s)
print(result)
