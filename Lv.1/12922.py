def solution(n):
    answer_list = []
    result = n // 2
    plus = n%2
    
    for i in range(0,result):
        answer_list.append("수박")
    
    if plus == 1:
        answer_list.append("수")
    
    answer = ''.join(answer_list)
    return answer