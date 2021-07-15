#https://www.hackerrank.com/challenges/string-construction/problem?h_r=next-challenge&h_v=zen

def str_cons(s):
    char_count = [0] * 26
    min_cost = 0
    for i in s:
        char_count[ord(i) - ord('a')] = 1
    for i in range(26):
        min_cost += char_count[i]
    return min_cost


q = int(input().rstrip())
for _ in range(q):
    S = input().rstrip()
    print(str_cons(S))
