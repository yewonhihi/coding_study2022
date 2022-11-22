# 부품 찾기

n = int(input())
dataN = list(map(int, input().split()))
m = int(input())
dataM = list(map(int, input().split()))

dataN.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid-1
        else:
            start = mid+1
        
    return 0
    
for i in dataM:
    if binary_search(dataN, i, 0, n-1) == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')