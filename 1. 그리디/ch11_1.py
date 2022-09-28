n = int(input())
data = list(map(int, input().split()))

result = 0
count = [0] * n

for i in range(1, n+1):
    count[i-1] = data.count(i)

for i in range(1, n+1):
    if count[i-1] >= i:
        result += (count[i-1] // i) 

print(result)