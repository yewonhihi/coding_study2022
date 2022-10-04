# 문자열 뒤집기

num = list(map(int, input()))
countZero = 0
countOne = 0

temp = 0
for i in num:  # 다 0으로 바꾸기
    if i==1 and temp==0:
        countZero += 1
        temp = 1
    elif i==0 and temp==1:
        temp = 0
    else: pass

temp = 1
for i in num:  # 다 1로 바꾸기
    if i==0 and temp==1:
        countOne += 1
        temp = 0
    elif i==1 and temp==0:
        temp = 1
    else: pass
        
print(min(countOne, countZero))