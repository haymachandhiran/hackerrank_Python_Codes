# #https://www.hackerrank.com/challenges/largest-permutation/problem
#
# def largest_pal(arr, n, k):
#     if k >= n:
#         return sorted(arr, reverse=True)
#     for i in range(k):
#         temp = arr[:]
#         maximum = max(arr[i:])
#         max_pos = arr.index(maximum)
#         arr[max_pos] = arr[i]
#         arr[i] = maximum
#         print(temp)
#         print(arr)
#         if temp == arr:
#             k += 1
#     return arr
#
#
# n, k = input().split()
# n = int(n)
# k = int(k)
# arr = list(map(int, input().split()))
# op = largest_pal(arr, n, k)
# op = list(map(str, op))
# print(f"{' '.join(op)}")


def KswapPermutation(arr, n, k):
    # Auxiliary array of storing the position of elements
    pos = {}
    for i in range(n):
        pos[arr[i]] = i

    for i in range(n):

        # If K is exhausted then break the loop
        if k == 0:
            break

        # If element is already largest then no need to swap
        if (arr[i] == n - i):
            continue

        # Find position of i'th largest value, n-i
        temp = pos[n - i]

        # Swap the elements position
        pos[arr[i]] = pos[n - i]
        pos[n - i] = i

        # Swap the ith largest value with the value at
        # ith place
        arr[temp], arr[i] = arr[i], arr[temp]

        # Decrement K after swap
        k = k - 1


# Driver code
n, k = input().split()
n = int(n)
k = int(k)
arr = list(map(int, input().split()))
KswapPermutation(arr, n, k)

# Print the answer
print(f"{' '.join(map(str, arr))}")