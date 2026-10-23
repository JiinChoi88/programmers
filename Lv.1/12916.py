def solution(s):
    answer = True
    
    s_list = list(s)
    size = len(s_list)
    p_count = 0
    y_count = 0
    
    for i in range(0,size):
        if (s_list[i] == 'p')or (s_list[i] == 'P'):
            p_count += 1
        elif (s_list[i] == 'y')or(s_list[i] == 'Y'):
            y_count += 1
    
    print(p_count)
    print(y_count)
    if (p_count == 0)and(y_count == 0):
        return True
    elif p_count == y_count:
        return True
    else:
        return False