# Problem Statement-: Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#                                         1 2 3
#                                         4 5 6
#                                         9 8 9

#                                         The left-to-right diagonal = 1+5+9 = 15, The right to left diagonal = 3+5+9 = 17, Their absolute difference is |15-17| = 2

# Function Description:

# diagonalDifference takes the following parameter:

# int arr[n][m]: an array of integers
# Input Format:

# The first line contains a single integer, n the number of rows and columns in the square matrix arr Each of the next n lines describes a row, arr[i] and consists of n space-separated integers arr[i][j]
# Output Format:

# Return the absolute difference between the sums of the matrix’s two diagonals as a single integer.

t = int(input())
def diganoal_difference(arr,n):
  left=0
  right=0
  for i in range(n):
    left += arr[i][i]
    right += arr[i][n-i-1]
  return abs(left-right)



while(t>0):
  n = int(input())
  arr=[]
  for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
  print(arr)  
  print(diganoal_difference(arr, n))
  t-=1
