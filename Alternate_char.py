#https://www.hackerrank.com/challenges/alternating-characters/problem?h_r=next-challenge&h_v=zen

def alternatingCharacters(s):
    ac_str = s[0]
    for i in range(1, len(s)):
        if abs(ord(s[i-1]) - ord(s[i])) == 1:
            ac_str += s[i]
    return len(s) - len(ac_str)


q = int(input())

for q_itr in range(q):
    S = input().rstrip()
    print(alternatingCharacters(S))
