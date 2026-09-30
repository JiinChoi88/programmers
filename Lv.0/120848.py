def solution(n):
    answer = 0
    
    count = 0
    num = 1
    store = 1
    while n > store:
        store = num*store
        num += 1
        count += 1
        if n<store:
            count -=1
    answer = count   
    if n==1:
        answer = 1
    
    return answer