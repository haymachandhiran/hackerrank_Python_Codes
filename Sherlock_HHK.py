def decentNumber(n):
    z = n//3
    print(z)
    for x in range(z, -1, -1):
        y = (n - x*3)/5
        if y == int(y):
            return x * '555' + int(y) * '33333'
    else:
        return -1

# t = int(input())
# for _ in range(t):
x = int(input())
print(decentNumber(x))


# def sherlockBeast(N):
#     K = 5*((2*N)%3)
#     if K > N:
#         return -1
#     else:
#         return '5' * (N-K) + '3'*K