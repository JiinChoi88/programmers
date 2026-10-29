def solution(n):
    
    num_list = list(map(int, str(n)))
 
    size = len(num_list)
    answer_list = []
    
    for k in range(9,-1,-1):
        for i in range(0,size):
            if num_list[i] == k:
                answer_list.append(k)
    
    answer = int(''.join(map(str, answer_list)))
    
    return answer
