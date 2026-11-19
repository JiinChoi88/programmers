def solution(words):
	answer = ''
	size = len(words)
	for i in range(0,size,1):
		words_size = len(words[i])
		if words_size >= 5:
			answer += words[i]

	if len(answer)==0:
		return "empty"
	else:
		return answer
	

words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1)

print("solution 함수의 반환 값은", ret1, "입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2)

print("solution 함수의 반환 값은", ret2, "입니다.")