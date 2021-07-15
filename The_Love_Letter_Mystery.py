#https://www.hackerrank.com/challenges/the-love-letter-mystery/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def mystery(s):
    rev = s[::-1]
    tot = 0
    for i in range(len(s)//2):
        if s[i] != rev[i]:
            tot += abs(ord(s[i]) - ord(rev[i]))
    return tot


q = int(input().rstrip())
for _ in range(q):
    S = input().rstrip()
    print(mystery(S))
