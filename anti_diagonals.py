# Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

# For Example:
# If the matrix is    

# 1 2 3
# 4 5 6
# 7 8 9
# The output should Return the following :

# [ 
#   [1],
#   [2, 4],
#   [3, 5, 7],
#   [6, 8],
#   [9]
# ]
# i.e print the elements of array diagonally.

# Note: The input array given is in single line and you have to output the answer in one line only.


# Input:

# The first line contains an integer T, depicting total number of test cases. 
# Then following T lines contains an integer N depicting the size of square matrix and next line followed by the value of array.


# Output:

# Print the elements of matrix diagonally in separate line.


# Constraints:

# 1 ≤ T ≤ 30
# 1 ≤ N ≤ 20
# 0 ≤ A[i][j] ≤ 9


# Example:

# Input:
# 2
# 2
# 1 2 3 4
# 3
# 1 2 3 4 5 6 7 8 9
# Output:
# 1 2 3 4
# 1 2 4 3 5 7 6 8 9


from itertools import islice

T = int(input())


def anti_diagonals(arr, n):
    result = []
    for col in range(N):
        start_col = col
        start_row = 0
        while (start_col >= 0 and start_row < N):
            result.append(arr[start_row][start_col])
            start_row += 1
            start_col -= 1
    for row in range(1, N):
        start_col = N - 1
        start_row = row
        while (start_col >= 0 and start_row < N):
            result.append(arr[start_row][start_col])
            start_row += 1
            start_col -= 1
    result=list(map(str, result))
    return ' '.join(result)


while (T > 0):
    N = int(input())
    arr = list(map(int, input().split()))
    brr = iter(arr)
    arr = [list(islice(brr, N)) for _ in range(N)]
    print(arr)
    print(anti_diagonals(arr, N))
