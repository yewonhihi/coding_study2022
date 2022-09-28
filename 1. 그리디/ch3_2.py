n, m, k = map(int, input().split())

num = list(map(int, input().split()))
num.sort()
count = k
result = 0

for _ in range(m):
    if count > 0 :
        result += num[n-1]
        count -= 1
    else :
        result += num[n-2]
        count = k
        
print(result)