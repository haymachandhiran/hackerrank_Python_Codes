from itertools import permutations as p


def check_Anagram_of_pal(s):
    char_count = [0] * 26
    odd_count = 0
    for i in s:
        char_count[ord(i) - ord('a')] += 1
    #print(char_count)
    for c in char_count:
        if c % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return 'NO'
    return 'YES'


s = input()
print(check_Anagram_of_pal(s))
