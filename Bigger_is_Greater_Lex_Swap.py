# from itertools import permutations
#
#
# def biggerIsGreater(w):
#     # print(w)
#     sw = sorted(w, reverse=True)
#     sort_w = ''.join(sw)
#     # print(f"Sorted = {sort_w}")
#     if w == sort_w:
#         return 'no answer'
#     else:
#         res = []
#         perm = permutations(w)
#         for i in list(perm):
#             res.append(''.join(i))
#         res = set(res)
#         res = list(res)
#         res.sort()
#         # print(res)
#         x = res.index(w)
#         # print(x)
#         return res[x + 1]

# def biggerIsGreater(w):
#     # print(w)
#     n = len(w)
#     sw = sorted(w, reverse=True)
#     sort_w = ''.join(sw)
#     # print(f"Sorted = {sort_w}")
#     if w == sort_w:
#         return 'no answer'
#     else:
#         for i in range(n-1, 0, -1):
#             for j in range(i-1, -1, -1):
#                 if w[i] <= w[j]:
#                     pass
#                 else:
#                     print(i)
#                     print(j)
#                     print(w[i])
#                     print(w[j])
#                     temp1 = w[0:j]+w[i]+w[j+1:]
#                     print(temp1)
#                     temp2 = temp1[0:i]+w[j]+temp1[i+1:]
#                     print(temp2)
#                     res = temp2[0:j+1]+''.join(sorted(temp2[j+1:]))
#                     return res

#working function

def biggerIsGreater(w):
    w = list(w)
    # Find non-increasing suffix
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    if i <= 0:
        return 'no answer'

    # Find the rightmost successor to pivot in the suffix
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        j -= 1

    # Swap the pivot with the rightmost character
    w[i - 1], w[j] = w[j], w[i - 1]

    # Reverse the sufix
    w[i:] = w[len(w) - 1:i - 1:-1]

    return ''.join(w)

w = 'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw'
w1 = 'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm'
print(w)
result = biggerIsGreater(w)
if w1 == result:
    print(True)
else:
    print(False)
# print(f'Output = {result}')
print(result)

