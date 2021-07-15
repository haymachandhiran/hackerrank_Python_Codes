#https://www.hackerrank.com/challenges/electronics-shop/problem


from itertools import product


def getMoneySpent(keyboards, drives, b):
    res = list(product(keyboards,drives))
    possible_buy = []
    for i in res:
        if sum(i) <= b:
            possible_buy.append(sum(i))
    if possible_buy:
        return max(possible_buy)
    else:
        return -1


bnm = input().split()

b = int(bnm[0])

n = int(bnm[1])

m = int(bnm[2])

keyboards = list(map(int, input().rstrip().split()))

drives = list(map(int, input().rstrip().split()))

#
# The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
#

print(getMoneySpent(keyboards, drives, b))
