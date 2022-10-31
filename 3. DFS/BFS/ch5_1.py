n, m = map(int, input().split())
result = 0

graph = []
for _ in range(n):
    temp = list(map(int, input()))
    graph.append(temp)

def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False    
    
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)