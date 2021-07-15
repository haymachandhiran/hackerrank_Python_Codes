#https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0/?problemStatus=unsolved&problemType=full&difficulty[]=1&page=1&sortBy=submissions&query=problemStatusunsolvedproblemTypefulldifficulty[]1page1sortBysubmissions


def sort_freq(s):
    val = list(set(s))
    res = []
    print(val)
    for i in val:
        res.append([i, s.count(i)])
    sort_res = sorted(res, key=lambda x: x[1], reverse=True)
    print(sort_res)
    main_res = []
    for i in sort_res:
        temp = (str(i[0]) + ' ') * i[1]
        print(temp)
        main_res.extend(temp)
    return main_res


N = int(input())
S = list(map(int, input().split()))
print(*sort_freq(S), sep ='')
