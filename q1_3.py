from collections import deque             

n,m=[int(x) for x in input('').split()] #미로 세로, 가로
maze =[[int(x) for x in input('')] for _ in range(n)] #미로

dx = [-1,1,0,0] #좌표 변화량
dy= [0,0,-1,1]

path = [[0] * m for _ in range(n)] #경로 기록 지도
path[0][0] = 1 #시작칸도 1칸

q = deque()
q.append((0,0)) #출발 좌표
while q:
    x, y = q.popleft()
    for i in range(4):
        xf=x+dx[i]
        yf=y+dy[i]

        if 0 <= xf < n and 0 <= yf < m and maze[xf][yf] == 1 and path[xf][yf] == 0:
            path[xf][yf] = path[x][y] + 1
            q.append((xf, yf))

print(path[n - 1][m - 1]) #최단거리 출력



