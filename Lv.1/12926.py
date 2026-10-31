def solution(s, n):
    
    answer_list = list(s)
    num_list=[] #a = 97 #z = 122 #공백 = 32
   
    size = len(answer_list)
    for i in range(0,size,1):
        num_list.append(ord(answer_list[i])+n)
    
    result = []
    for k in range(0,size,1):
        if num_list[k]-n == 32: #공백처리
            result.append(" ")
        elif num_list[k] > 122:
            result.append(chr(num_list[k]-26))
        elif answer_list[k].isupper() and num_list[k] > 90:
            result.append(chr(num_list[k]-26))
        else:
            result.append(chr(num_list[k]))
    
    answer = "".join(result)
        
    return answer