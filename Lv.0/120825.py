def solution(my_string, n):
    result = []

    for i in range(len(my_string)):
        for k in range(n):
            result.append(my_string[i])

    answer = "".join(result)
    return answer