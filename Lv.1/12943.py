def solution(num):
    answer = 0
    if num == 1:
        return 0
    
    count = 0
    n = num
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            count += 1
        elif n % 2 == 1:
            n = n*3
            n += 1
            count += 1
        
        if count == 500:
            return -1
    
    return count
    