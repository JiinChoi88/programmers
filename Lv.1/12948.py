def solution(phone_number):
    answer = ''
    number = list(phone_number)
    size = len(number)
    num = size -4
    for i in range(0, num, 1):
        number[i] = '*'
        
    answer = ''.join(number)
    return answer