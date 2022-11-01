# 성적이 낮은 순서로 학생 출력하기

n = int(input())

dic = {}
for _ in range(n):
    a, b = input().split()
    b = int(b)
    dic[a] = b
    
