#https://practice.geeksforgeeks.org/problems/winner-of-an-election/0


def win(s):
    candidate = sorted(list(set(s)))
    print(candidate)
    print(s)
    res = {}
    for i in range(len(candidate)):
        temp = s.count(candidate[i])
        res[candidate[i]] = temp
    max_votes = max(list(res.values()))
    print(res)
    print(res)
    print(max_votes)
    for key, value in res.items():
        if value == max_votes:
            return key


N = int(input())
S = list(map(str, input().split()))
print(win(S))


#another method

# from collections import OrderedDict
#
#
# def win(s):
#     candidate = list(set(s))
#     res = {}
#     for i in range(len(candidate)):
#         temp = s.count(candidate[i])
#         res[candidate[i]] = temp
#     max_votes = max(list(res.values()))
#     res1 = OrderedDict(sorted(res.items()))
#     for key, value in res1.items():
#         if value == max_votes:
#             return key
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     S = list(map(str, input().split()))
#     print(win(S))
