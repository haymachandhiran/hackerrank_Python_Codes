#https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

from statistics import median


#2 3 4 2 3 6 8 4 5
def fraud(n, d, exp):
    notification = 0
    for i in range(d, n):
        temp = median(exp[i-d: i])

        if exp[i] >= (2 * temp):
            notification += 1
    return notification


N, D = input().split()
N = int(N)
D = int(D)
EXP = list(map(int, input().split()))
print(fraud(N, D, EXP))





# def sort(array):
#     """Sort the array by using quicksort."""
#
#     less = []
#     equal = []
#     greater = []
#
#     if len(array) > 1:
#         pivot = array[0]
#         for x in array:
#             if x < pivot:
#                 less.append(x)
#             elif x == pivot:
#                 equal.append(x)
#             elif x > pivot:
#                 greater.append(x)
#         # Don't forget to return something!
#         return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
#     # Note that you want equal ^^^^^ not pivot
#     else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
#         return array

