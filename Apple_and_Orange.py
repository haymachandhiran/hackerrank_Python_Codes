#https://www.hackerrank.com/challenges/apple-an

def countApplesAndOranges(s, t, a, b, apples, oranges):
    tot_apple = 0
    tot_orange = 0
    for i in range(len(apples)):
        if (a + apples[i]) in range(s, t+1):
            tot_apple += 1
    for i in range(len(oranges)):
        if (b + oranges[i]) in range(s, t+1):
            tot_orange += 1
    print(tot_apple)
    print(tot_orange)


st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)