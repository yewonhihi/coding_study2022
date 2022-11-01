# 연구소 *

n, m = map(int, input().split())
data = []

for _ in range(n):
    temp = list(map(int, input().split()))
    data.append(temp)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

