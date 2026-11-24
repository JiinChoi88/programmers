# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

def solution(scores):
	answer = 0
	max_num = max(scores)
	min_num = min(scores)
	scores.remove(max_num)
	scores.remove(min_num)
	size = len(scores)
	total = 0
	for i in range(0,size,1):
		total += scores[i]

	answer = (total // size)
	return answer

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")