def solution(x, n):
    answer = []
    answer.append(x)
    count = 0
    i = 2
    while count != n-1:
        answer.append(x*i)
        i+=1
        count += 1
    
    return answer