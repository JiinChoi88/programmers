# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(price, grade):
	answer = 0
	num = 0
	if grade == "V":
		num = 15
	elif grade == "G":
		num = 10
	else:
		num = 5

	answer = price * (1-num/100)
	return f"{answer:.0f}"