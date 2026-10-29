def solution(seoul):
    answer = ''
    size = len(seoul)
    for i in range(0,size,1):
        if seoul[i] == "Kim":
            num = str(i)
            return "김서방은 "+num+"에 있다"