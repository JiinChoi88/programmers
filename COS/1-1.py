# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(shirt_size):
	size = len(shirt_size)
	a = 0
	b = 0
	c = 0
	d = 0
	e = 0
	f = 0
	answer = []
	for i in range(0,size,1):
		if shirt_size[i] == "XS":
			a += 1
		elif shirt_size[i] == "S":
			b += 1
		elif shirt_size[i] == "M":
			c += 1
		elif shirt_size[i] == "L":
			d += 1
		elif shirt_size[i] == "XL":
			e += 1
		else:
			f += 1
	answer.append(a)
	answer.append(b)
	answer.append(c)
	answer.append(d)
	answer.append(e)
	answer.append(f)
	
	
	return answer