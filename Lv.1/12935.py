def solution(arr):
    answer = []
    size = len(arr)
    if size == 1:
        return [-1]
    
    minn = arr[0]
    for i in range(0,size):
        answer.append(arr[i])
        if minn > arr[i]:
            minn = arr[i]
    
    for i in range(0,size):
        if minn == answer[i]:
            answer.pop(i)
            break
    return answer