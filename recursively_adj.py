a='aaabccddd'
#a='miiipie'
#a='acbbacbbaa'
#a = aaabccddd 
def adj(a):
  res_lat=a
  a+=' '
  temp,res='',''
  for i in range(len(a)-1):
    if a[i]==a[i+1] or a[i] in temp:
      pass
    else:
      res += a[i]
    temp=a[i]
  print(res)	
  if res_lat==res:
    if res:
      return res
    else:
      return 'Empty String'
  else:
    res_lat=res
    return adj(res) 
print(adj(a))