def solution(s):
    answer = ''
    nums = list(map(int, s.split()))
    size = len(nums)
    min_num = nums[0]
    max_num = nums[0]
    for i in range(0, size):
        if min_num > nums[i]:
            min_num = nums[i]
        if max_num < nums[i]:
            max_num = nums[i]
    
    answer = ' '.join(map(str, [min_num, max_num]))
    return answer