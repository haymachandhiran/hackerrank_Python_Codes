#https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    zone = (s[-2:])
    print(zone)
    a = s[0:8]
    print(a)
    b = a.split(':')
    print(b)
    x = int(b[0])
    if zone == 'AM':
        if x == 12:
            b[0] = '00'
    else:
        if x != 12:
            x += 12
            b[0] = str(x)
    return ':'.join(b)

# s = input()
s = '07:05:45PM'
result = timeConversion(s)
print(result)
