# 거스름돈

a = int(input())
money = [500, 100, 50, 10]

result = 0

for i in money:
    result += (a // i)
    a %= i

print(result)