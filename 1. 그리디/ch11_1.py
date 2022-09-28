# 모험가 길드

n = int(input())
data = list(map(int, input().split()))

result = 0
count = [0] * n  # 숫자 개수를 넣을 리스트

# 개수 입력
for i in range(1, n+1):
    count[i-1] = data.count(i)

for i in range(1, n+1):
    
    # 개수가 해당 숫자 이상일 때 숫자로 나누어 몫이 만들 수 있는 그룹 수가 된다
    if count[i-1] >= i:
        result += (count[i-1] // i) 

print(result)