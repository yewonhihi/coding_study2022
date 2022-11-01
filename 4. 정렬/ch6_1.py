# 위에서 아래로

n = int(input())

num = []
for _ in range(n):
    temp = int(input())
    num.append(temp)

num.sort(reverse=True)

for i in range(n):
    
    print(num[i], end=" ")