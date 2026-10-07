def solution(arr):
    answer = 0
    size = len(arr)
    
    summ = 0
    for i in range (0,size):
        summ += arr[i]
    
    answer = summ/size
    return answer