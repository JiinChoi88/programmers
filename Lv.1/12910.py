def solution(arr, divisor):
    answer = []
    size = len(arr)
    count = 0
    for i in range(0, size, 1):
        if arr[i]%divisor == 0:
            answer.append(arr[i])
            count += 1
    
    if count == 0:
        answer.append(-1)
        return answer
    
    # 오름차순 정리
    
    size2 = len(answer)
    result = []
    while size2 != 0:
        min_num = min(answer)
        result.append(min_num)
        answer.remove(min_num)
        size2 -= 1
        
    return result