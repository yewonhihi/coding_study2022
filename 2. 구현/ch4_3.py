# 왕실의 나이트

data = input()
row = int(data[1])
# ord() : 문자의 유니코드 값을 돌려주는 함수
column = int(ord(data[0])) - int(ord('a')) + 1

steps = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

result = 0

for step in steps:
    nx = row + step[0]
    ny = column + step[1]
    
    if nx < 1 or ny < 1 or nx > 8 or ny > 8 :
        continue
    
    result += 1

print(result)