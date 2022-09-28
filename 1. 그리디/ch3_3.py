# 숫자 카드 케임

n, m = map(int, input().split())

result = 0

for i in range(n):
    num = list(map(int, input().split()))
    minValue = min(num)
    if minValue > result:
        result = minValue
    
print(result)