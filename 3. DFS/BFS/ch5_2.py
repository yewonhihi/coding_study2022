from collections import deque

n, m = map(int, input().split())
result = 0

graph = []
for _ in range(n):
    temp = list(map(int, input()))
    graph.append(temp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            
            if graph[nx][ny]==0:
                continue
            
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    
    return graph[n-1][m-1]
        

#while(x==n-1 and y==m-1):
#        if graph[x+1][y]==1:
#            x += 1 
#        elif graph[x][y+1]==1:
#            y += 1
#        elif graph[x-1][y]==1:
#            x -= 1
#        elif graph[x][y-1]==1:
#            y -= 1
#        else: 
#            print('error')
            
#        result += 1

print(solution(0,0))