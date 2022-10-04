# 무지의 먹방 라이브

def solution(food_times, k):
    time = 0
    i = 0
    m = len(food_times)  # 최대 index
    
    if sum(food_times) <= k: return -1
    
    while(1):
        if time==k: break
        if i==m:
            i = 0
            continue
        if food_times[i]==0: continue
        food_times[i] -= 1
        time += 1
        i += 1
    
    return i


print(solution([3,1,2], 5))