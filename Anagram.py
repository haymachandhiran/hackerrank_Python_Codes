#https://www.hackerrank.com/challenges/anagram/problem

def anagram(s):
    l = len(s)
    if l % 2 == 1:
        return -1
    else:
        change = 0
        s1 = s[0:l//2]
        s2 = s[l//2:]
        print(s1)
        print(s2)
        for i in range(l//2):
            print(s2)
            x = s2.find(s[i])
            if x == -1:
                change += 1
            else:
                s2 = s2[:x] + s2[x+1:]
        return change


q = int(input())
while q != 0:
    S = input().rstrip()
    print(anagram(S))
    q -= 1
