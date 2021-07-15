#https://www.hackerrank.com/challenges/weighted-uniform-string/problem

# def weightedUniformStrings(s, q):
#     count = 1
#     tot_weight = []
#     res = []
#     tot_weight.append(ord(s[0]) - 97 + 1)
#     for i in range(1, len(s)):
#         weight = ord(s[i]) - 97 + 1
#         if s[i] == s[i-1]:
#             count += 1
#         else:
#             count = 1
#         tot_weight.append(weight * count)
#     for j in q:
#         if j not in tot_weight:
#             res.append('No')
#         else:
#             res.append('Yes')
#     return res

def weightedUniformStrings(s, queries):
    weights = []
    prev = -1
    length = 0
    for c in s:
        weight = ord(c) - ord('a') + 1
        weights.append(weight)
        if prev == c:
            length += 1
            weights.append(length * weight)
        else:
            prev = c
            length = 1
        print(weights)
    rval = []
    for q in queries:
        if q in weights:
            rval.append("Yes")
        else:
            rval.append("No")
    return rval


s = 'aaabbbbcddd'
print(s)
q = [9, 7, 8, 12, 5]
print('\n'.join(weightedUniformStrings(s, q)))
