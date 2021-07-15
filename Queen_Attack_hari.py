from itertools import product
N=5
O=[(3,2),(3,3),(3,4),(4,2),(4,4),(5,2),(5,3)]
pos=(4,3)
cb=product(range(1,N+1),repeat=2)
q=[]
for p in cb:
  if (abs(p[0]-pos[0])==abs(p[1]-pos[1]) or p[0]==pos[0] or p[1]==pos[1]) and p!=pos:
    q.append(p)

def obs(x,y,a,b,q):
     while True:
        if (x,y) not in q:
          break
        q.remove((x,y))
        x+=a
        y+=b

for i in O:
  if i[0]==pos[0] or i[1]==pos[1] or abs(i[0]-pos[0])==abs(i[1]-pos[1]):
    x,y=i[0],i[1]
    if i[0]==pos[0] and i[1]>pos[1]:
      obs(x,y,0,1,q)
    elif i[0]==pos[0] and i[1]<pos[1]: 
      obs(x,y,0,-1,q)
    elif i[0]>pos[0] and i[1]==pos[1]:
      obs(x,y,1,0,q)
    elif i[0]<pos[0] and i[1]==pos[1]:
      obs(x,y,-1,0,q)
    elif i[0]>pos[0] and i[1]>pos[1]:
      obs(x,y,1,1,q)
    elif i[0]<pos[0] and i[1]<pos[1]:
      obs(x,y,-1,-1,q)
    elif i[0]>pos[0] and i[1]<pos[1]:
      obs(x,y,1,-1,q)
    else:
      obs(x,y,-1,1,q)
print(q,len(q))