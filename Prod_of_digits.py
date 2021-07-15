#multiply all digits in a given number and print output
#If negative number is there, print - Number is not valid, please enter positive number

s = int(input())
if s < 0:
    print('Number is not valid, please enter positive number')
else:
    c = str(s)
    res = 1
    for i in c:
        res = res * int(i)
        print(res)
