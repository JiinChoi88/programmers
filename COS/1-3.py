# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def func_a(month, day):
	month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	total = 0
	for i in range(0,month-1,1):
		total += month_list[i]
	total += day
	return total - 1