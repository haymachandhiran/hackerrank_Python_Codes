def pair_of_sum(arr, brr, N, M, X):
    comp = []
    pair = {}
    # ret = []
    # arr.sort()
    # print(arr)
    for i in range(N):
        comp.append(X - arr[i])
        if comp[i] in brr:
            pair[arr[i]] = comp[i]
    return pair


T = int(input())
while (T > 0):
    N, M, X = input().split()
    N = int(N)
    M = int(M)
    X = int(X)
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    op = pair_of_sum(A, B, N, M, X)

    op = sorted(op.items())
    if op:

        for i in op:
            if i == op[-1]:
                print(i[0], i[1], end='')
            else:
                print(i[0], i[1], end=', ')
    else:
        print(-1)

    # print(op)
    # res_dct = {op[i]: op[i + 1] for i in range(0, len(op), 2)}
    # print(res_dct)
    # res = []
    # for key, value in op.items():
    #     res.append(str(key) + " " + str(value))
    # # print(res)
    # if res:
    #     print(', '.join(res))
    # else:
    #     print(-1)
    T -= 1
