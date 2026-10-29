def solution(s):
    answer = ''
    
    ord_list = []
    result = []
    s_list = list(s)
    size = len(s_list)
    
    for i in range(0,size,1):
        ord_list.append(ord(s_list[i]))
    
    for k in range(0,size,1):
        max_num = max(ord_list)
        result.append(chr(max_num))
        ord_list.remove(max_num)
    
    answer = ''.join(result)
    
    return answer