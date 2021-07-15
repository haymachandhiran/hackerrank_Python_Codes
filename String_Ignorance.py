#https://practice.geeksforgeeks.org/problems/string-ignorance/0/?category[]=Arrays&category[]=Strings&category[]=Arrays&category[]=Strings&problemType=full&difficulty[]=-1&difficulty[]=0&difficulty[]=1&page=1&sortBy=newest&query=category[]Arrayscategory[]StringsproblemTypefulldifficulty[]-1difficulty[]0difficulty[]1page1sortBynewestcategory[]Arrayscategory[]Strings#

import sys
for _ in range(int(input())):
    s = input()
    s_dummy = s.lower()
    res = ''
    alpha = [0] * 26
    sp = 0
    for i in range(len(s_dummy)):
        if s_dummy[i].isalpha():
            alpha[ord(s_dummy[i]) - 97] += 1
            if alpha[ord(s_dummy[i]) - 97] % 2 != 0:
                res += s[i]
        elif s_dummy[i] == ' ':
            sp += 1
            if sp % 2 != 0:
                res += s[i]
    print(res)

