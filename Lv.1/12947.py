def solution(x):
    answer = True
    x_list = list(map(int, str(x)))
    size = len(x_list)
    
    num = 0
    for i in range(0,size):
        num += x_list[i]
    
    if x%num ==0:
        return True
    else:
        return False
    