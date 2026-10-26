def solution(n):
    answer = []
    n_list = list(map(int,str(n)))
    size = len(n_list)
    c = 0
    for i in range(size-1,-1,-1):
        answer.append(n_list[i])
    return answer