# 특정 거리의 도시 찾기 *

from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    nx = q.popleft()
    for i in graph[nx]:
        if distance[i] == -1:
            distance[i] = distance[nx]+1
            q.append(i)
            
check = False
for i in range(1, n+1):
    if distance[i]==k:
        print(i)
        check = True
        
if check == False:
    print("-1")