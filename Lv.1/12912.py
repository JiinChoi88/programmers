def solution(a, b):
    answer = 0
    if a == b:
        return a
    c = a
    if a > b:
        a = b
        b = c
        
    for i in range(a,b+1,1):
        answer += i
    return answer