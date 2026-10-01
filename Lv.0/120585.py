def solution(array, height):
    size = len(array)
    count = 0
    for i in range(0,size):
        if array[i]>height:
            count+=1
    answer = count
    return answer