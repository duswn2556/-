n,m=[int(x) for x in input('').split()]
tray=[[int(x) for x in input('')] for _ in range(n)]

def dfs(x,y):
    if 0 <= x < n and 0 <= y < m and tray[x][y] == 0:
        tray[x][y] = 'v'
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

cnt=0
for i in range(n):
    for j in range(m):
        if tray[i][j] == 0:
            dfs(i,j)
            cnt+=1

print(cnt)
