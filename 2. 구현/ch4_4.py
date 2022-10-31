# 게임 개발 *

n, m = map(int, input().split())
x, y, way = map(int, input().split())
data = [[0] * m for _ in range(n)]

for i in n:
    temp = map(int, input().split())
    for j in m:
        data[i, j] = temp[j]
    
steps = [(-1,0), (0,1), (1,0), (0,-1)]
result = 0

#while True
    