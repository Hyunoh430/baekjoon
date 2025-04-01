from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # (현재 값, 인덱스)
    count = 0

    while queue:
        current_sum, idx = queue.popleft()

        # 모든 숫자를 처리한 경우
        if idx == len(numbers):
            if current_sum == target:
                count += 1
        else:
            # 숫자를 더하는 경우와 빼는 경우
            queue.append((current_sum + numbers[idx], idx + 1))
            queue.append((current_sum - numbers[idx], idx + 1))
    
    return count
