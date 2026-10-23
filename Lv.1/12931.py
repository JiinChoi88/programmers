def solution(n):
    answer = 0

    l = list(map(int, str(n)))
    
    size = len(l)
    
    for i in range(0,size):
        answer += l[i]

    return answer