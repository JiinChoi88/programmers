# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def func_a(scores, score):
	rank = 1
	for s in scores:
		if s == score:
			return rank
		rank += 1
	return 0

def func_b(arr):
	arr.sort(reverse=True)

def func_c(arr, n):
	return arr[n]

def solution(scores, n):
	score = func_c(scores,n)
	func_b(scores)
	answer = func_a(scores,score)
	return answer