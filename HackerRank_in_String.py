#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

def hackerrankInString(s):
    hack = 'hackerrank'
    temp = s
    for i in hack:
        # print(temp)
        if temp.find(i) == -1:
            return 'NO'
        else:
            x = temp.find(i)
            temp = temp[x+1:]
    return 'YES'


s = 'hackerworldrank'
print(hackerrankInString(s))
#s = "hackerworld"
print(ord(' '))
