def solution(s):
    answer = list(s)
    size = len(answer)
    result2= []
    if size % 2 == 0:
        num = size // 2
        for i in range(num-1, num+1):
            result2.append(answer[i])
        result = ''.join(result2)
    else:
        num = size//2
        result = ''.join(answer[num])
    return result