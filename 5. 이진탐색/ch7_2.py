# 떡볶이 떡 만들기

n, target = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
mid = (start+end) // 2

def slicing(cut):
    total = 0
    for i in data:
        if i>cut:
            total += i-cut
    
    return total

while start <= end:
    mid = (start+end) // 2
    if slicing(mid) == target:
        break
    elif slicing(mid) > target:
        start = mid+1
    else:
        end = mid-1

print(mid)