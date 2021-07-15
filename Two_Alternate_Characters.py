#https://www.hackerrank.com/challenges/two-characters/problem


from itertools import combinations


def two_alt_char(s):
    res = []
    res_len = 0
    unique_char = list(set(s))
    comb = list(combinations(unique_char, 2))
    # print(comb)
    for i in range(len(comb)):
        temp = []
        temp_len = 0
        for j in range(len(s)):
            if s[j] in comb[i]:
                if j == 0:
                    temp.append(s[j])
                else:
                    if not temp:
                        temp.append(s[j])
                    elif temp[-1] == s[j]:
                        temp.clear()
                        break
                    else:
                        temp.append(s[j])
        if temp:
            if len(temp) > res_len:
                res = temp
                res_len = len(temp)
    # print(res)
    if res:
        return res_len
    else:
        return 0


S = 'asvkugfiugsalddlasguifgukvsa'
print(S)
print(two_alt_char(S))

#asdcbsdcagfsdbgdfanfghbsfdab -     8

#asvkugfiugsalddlasguifgukvsa -     0

#  pvmaigytciycvjdhovwiouxxylkxjjyzrcdrbmokyqvsradegswrezhtdyrsyhg --- 6


a = ()
a.in
