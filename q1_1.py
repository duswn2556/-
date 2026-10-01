n=int(input(''))
plan=input('').split()

x,y=1,1
dct={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
for i in plan:
    if i not in dct:
        continue
    if i in dct:
        dx,dy=dct[i]
        xf,yf=x+dx,y+dy
        if 1<=xf<=n and 1<=yf<=n:
            x,y=xf,yf
            
print(x,y)



