# 곱하기 혹은 더하기

num = list(map(int, input()))
result = 1

for i in num:
    if i==0: pass
    else: result *= i
    
print(result)