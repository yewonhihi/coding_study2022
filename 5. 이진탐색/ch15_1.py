# 정렬된 배열에서 특정 수의 개수 구하기 *

n, x = map(int, input().split())
data = list(map(int, input().split()))

def search(arr, target, l):
    
    first=searchFirst(arr, target, 0, l-1)
    if first == None:
        return -1
    
    last=searchLast(arr, target, 0, l-1)
    
    return last-first+1

def searchFirst(arr, target, start, end):
    mid = (start+end) // 2
    if start > end:
        return None
    
    if (mid==0 or arr[mid-1]<target) and arr[mid]==target:
        return mid
    elif arr[mid] >= target:
        return searchFirst(arr, target, start, mid-1)
    else:
        return searchFirst(arr, target, mid+1, end)
    
def searchLast(arr, target, start, end):
    mid = (start+end) // 2
    if start > end:
        return None
    if (mid==n-1 or arr[mid+1]>target) and arr[mid]==target:
        return mid
    elif arr[mid] > target:
        return searchLast(arr, target, start, mid-1)
    else:
        return searchLast(arr, target, mid+1, end)
    
print(search(data, x, n))