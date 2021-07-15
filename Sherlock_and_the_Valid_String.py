#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_r=next-challenge&h_v=zen


def check_valid(s):
    char_count = [0] * 26
    for i in s:
        char_count[ord(i) - ord('a')] += 1
    print(char_count)
    set_count = set(char_count)
    set_count = list(set_count)
    if 0 in set_count:
        set_count.remove(0)
    print(set_count)
    if len(set_count) > 2:
        return 'NO'
    elif len(set_count) == 1:
        return 'YES'
    elif 1 in char_count:
        if char_count.count(1) == 1:
            return 'YES'
        else:
            return 'NO'
    else:
        if abs(set_count[0] - set_count[1]) == 1:
            return 'YES'
        else:
            return 'NO'


S = input().rstrip()
print(check_valid(S))
#aaaabbcc
