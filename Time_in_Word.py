from num2words import num2words


def timeInWords(h, m):
    if m == 00:
        return num2words(h)+" o' clock"
    if m > 30:
        h += 1
        if h > 12:
            h -= 12
        m = 60 - m
        if m == 15:
            return "quarter to "+num2words(h)
        else:
            x = num2words(m)
            x = x.replace('-', ' ')
            return x+" minutes to "+num2words(h)
    else:
        if m == 15:
            return "quarter past "+num2words(h)
        else:
            x = num2words(m)
            x = x.replace('-', ' ')
            return x+" past "+num2words(h)


h = int(input().strip())
m = int(input().strip())
result = timeInWords(h, m)
print(result)
