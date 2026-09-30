def solution(box, n):
    dice1 = box[0]//n
    dice2 = box[1]//n
    dice3 = box[2]//n
    
    answer = dice1*dice2*dice3
    return answer