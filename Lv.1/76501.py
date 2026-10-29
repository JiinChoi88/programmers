def solution(absolutes, signs):
    answer = 0
    size = len(absolutes)
    
    for i in range(0,size,1):
        if signs[i] == False:
            answer -= absolutes[i]
        else:
            answer += absolutes[i]
    return answer