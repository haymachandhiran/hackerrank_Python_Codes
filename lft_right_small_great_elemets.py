x = [4,3,2,7,8,9]

def check(x):
  for i in range(1,len(x)-1):
    for j in range(i):
        l=0
        if x[j] < x[i]:
            pass
        else:
            l=1
            break
    if l==0:
        #print(x[i])
        m=0
        for k in range(i+1,len(x)):
            if x[i] < x[k]:
                pass
            else:
                m=1
                break
        if m==0:
            return x[i]
  return -1

print(check(x))

# print(*(check(x)),sep  = ',')


#for i in range(4):
#    print(x[i])
