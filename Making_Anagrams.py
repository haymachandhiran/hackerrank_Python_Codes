#https://www.hackerrank.com/challenges/making-anagrams/problem

#from collections import Counter


def make_anagram(s1, s2):
    change = 0
    for i in range(len(s1)):
        x = s2.find(s1[i])
        if x == -1:
            pass
        else:
            change += 1
            s2 = s2[:x] + s2[x+1:]
    print(s1, s2, change)
    return len(s1) + len(s2) - change


S1 = input().rstrip()
S2 = input().rstrip()
print(make_anagram(S1, S2))

