n,m=[int(x) for x in input('').split()] #세로, 가로 길이
tray=[[int(x) for x in input('')] for _ in range(n)] #얼음틀

def dfs(x,y):
    if 0 <= x < n and 0 <= y < m and tray[x][y] == 0:
        tray[x][y] = 'v' #방문처리
        dfs(x - 1, y) #연쇄재귀탐색
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

cnt=0 #카운트변수
for i in range(n):
    for j in range(m):
        if tray[i][j] == 0: #방문 안 한 구멍
            dfs(i,j)
            cnt+=1

print(cnt) #총 아이스크림 개수
