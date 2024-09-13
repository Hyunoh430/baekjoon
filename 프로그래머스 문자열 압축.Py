def solution(s):
    min_result = len(s)  # 초기값을 문자열 길이로 설정
    
    for test_length in range(1, len(s) // 2 + 1):  # 1부터 문자열 길이의 절반까지
        result = 0
        count = 1
        prev = s[:test_length]
        
        for i in range(test_length, len(s), test_length):
            current = s[i:i+test_length]
            if prev == current:
                count += 1
            else:
                result += len(prev) + (len(str(count)) if count > 1 else 0)
                prev = current
                count = 1
        
        # 마지막 부분 처리
        result += len(prev) + (len(str(count)) if count > 1 else 0)
        
        min_result = min(min_result, result)
    
    return min_result