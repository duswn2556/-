n=int(input('')) #지도의 크기
plan=input('').split() #이동할 방향

x,y=1,1 #시작점
dct={'L':(0,-1),'R':(0,1),'U':(-1,0),'D':(1,0)}
for i in plan:
    if i not in dct:
        continue

    dx,dy=dct[i] #이동량
    xf,yf=x+dx,y+dy #이동 후 좌표
    if 1<=xf<=n and 1<=yf<=n:
        x,y=xf,yf
            
print(x,y) #최종 위치



