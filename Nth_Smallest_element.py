#https://www.youtube.com/watch?v=24r3iwM7I7U&list=PL7f0FYY_3hQDS79OekQv5PO7jCDGUaEyk&index=16


#Find Nth smallest element in a given array
#30 15 10 5 80 2 56 150

# arr = list(map(int, input().split()))
# n = int(input())
# arr.sort()
# print(arr[n-1])

#Another sum :
#Check square of a number's unit digit is same as the number's unit digit

# n = int(input())
# sq_n = n ** 2
# if (n % 10) == (sq_n % 10):
#     print('YES')
# else:
#     print('NO')
#


#Aonter Sum: Take string as input and determine the firrst char whether it is upper or lower or digit or symbol

s = input()
if s[0].isupper():
    print('UpperCase')
elif s[0].islower():
    print('LowerCase')
elif s[0].isdigit():
    print('Digit')
else:
    print('Symbol')