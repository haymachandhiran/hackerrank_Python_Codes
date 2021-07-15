#https://www.youtube.com/watch?v=0jhkft3Kv9Y&list=PL7f0FYY_3hQDS79OekQv5PO7jCDGUaEyk&index=7
#Take a arr len and array of  as ip
#Find how many ip contains only digits and how many contains only alpha
#Return  Invalid input if any input contains alphanum

# 5
# ab 345345 vasa 3535 34


n = int(input())
arr = list(map(str, input().split()))
digits = 0
alpha = 0
t = 0
for i in arr:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        alpha += 1
    else:
        t = 1
        break
if not t:
    print(f'Digits = {digits}')
    print(f'Alpha = {alpha}')
else:
    print('Invalid Input')


