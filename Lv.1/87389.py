def solution(n):
    
    problem = n-1
    count = 2
    while count != problem:
        if problem % count == 0 :
            break
        else:
            count += 1
    
    answer = count
    return answer