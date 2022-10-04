# 곱하기 혹은 더하기

num = list(map(int, input()))
result = num[0]

for i in num[1:]:
    if i <=1 or result <=1 : result += i
    else: result *= i
    
print(result)