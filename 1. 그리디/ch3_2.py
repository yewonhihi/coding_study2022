# 큰 수의 법칙

n, m, k = map(int, input().split())

num = list(map(int, input().split()))
num.sort()
count = k
result = 0

for _ in range(m):
    if count > 0 :
        result += num[n-1]
        count -= 1
    
    # 최대 더할 수 있는 횟수 초과시 두번쨰로 큰 수를 더해주고 count는 초기화해준다
    else :
        result += num[n-2]
        count = k
        
print(result)