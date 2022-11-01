# 미로 탐색
from collections import deque
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque([(0, 0)])
while q:
    x, y = q.pop()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
            continue
        
        if graph[nx][ny] != 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))
            continue
        
print(graph[n-1][m-1])