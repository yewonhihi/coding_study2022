# 상하좌우

n = int(input())
data = list(input().split())
X = 1
Y = 1

for i in data:
    if i=='L' : Y-=1
    elif i=='R' : Y+=1
    elif i=='U' : X-=1
    else : X+=1
    
    if X < 1 : X=1
    if Y < 1 : Y=1
    if X > n : X=n
    if Y > n : Y=n
    
print(X, Y)