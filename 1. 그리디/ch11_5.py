# 볼링공 고르기

n, m = map(int, input().split())
ball = list(map(int, input().split()))
ball.sort()
all = len(ball)
count = 0

for i in ball:
    count += (all-ball.count(i))

count //= 2
print(count)