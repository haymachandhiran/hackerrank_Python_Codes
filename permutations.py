from itertools import permutations


def allPermutations(str):
    # Get all permutations of string 'ABC'
    permList = permutations(str)
    ret= []
    for i in permList:
        print(i)
        ret.append(''.join(i))
    print(ret)
    return ret

T = int(input())

while (T > 0):
    S = input()
    res = allPermutations(S)
    print(' '.join(res))
    T -= 1