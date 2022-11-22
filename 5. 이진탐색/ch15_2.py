# 고정점 찾기

n = int(input())
data = list(map(int, input().split()))

def binary_search(arr, start, end):
    while start <= end:
        mid=(start+end)//2
        if arr[mid]==mid:
            return mid
        elif arr[mid] > mid:
            end = mid-1
        else:
            start = mid+1
    
    return -1

print(binary_search(data, 0, n-1))