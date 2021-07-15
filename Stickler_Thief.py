# def stickler_thief(a, n):
#     max_to_min = sorted(a,reverse=True)
#     print(max_to_min)
#     odd_tot = 0
#     even_tot = 0
#     for i in range(n):
#         if (i+1) % 2 == 0:
#             even_tot += a[i]
#         else:
#             odd_tot += a[i]
#     if odd_tot > even_tot:
#         return odd_tot
#     else:
#         return even_tot

def stickler_thief(a, n):
    max_to_min = sorted(a, reverse=True)
    print(max_to_min)
    tot_using_max = 0

    odd_tot = 0
    even_tot = 0
    for i in range(n):
        if (i+1) % 2 == 0:
            even_tot += a[i]
        else:
            odd_tot += a[i]
    if odd_tot > even_tot:
        return odd_tot
    else:
        return even_tot

T = int(input())
while T > 0:
    n = int(input())
    a = list(map(int, input().split()))
    print(stickler_thief(a, n))
    T -= 1



