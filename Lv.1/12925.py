def solution(s):
    answer_list = []
    answer = 0
    s_list = list(s)
    size = len(s_list)
    if s_list[0] == "-":
        for i in range(1, size, 1):
            answer_list.append(s_list[i])
        answer = -int(''.join(answer_list))
    elif s_list[0] == "+":
        for i in range(1, size, 1):
            answer_list.append(s_list[i])
        answer = int(''.join(answer_list))
    else:
        for i in range(0, size, 1):
            answer_list.append(s_list[i])
        answer = int(''.join(answer_list))
    return answer