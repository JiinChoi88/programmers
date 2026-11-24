# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def solution(words, word):
	count = 0
	word_list = list(word)
	word_len = len(word_list)
	size = len(words)
	
	for i in range(0,size,1):
		if words[i] != word:
			for k in range(0,word_len, 1):
				words_list = list(words[i])
				if word_list[k] != words_list[k]:
					count += 1

			
	return count

words = ["CODE", "COED", "CDEO"]
word = "CODE"
ret = solution(words, word)