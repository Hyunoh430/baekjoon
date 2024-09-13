def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        
        # 현재 숫자를 더하는 경우
        plus = dfs(index + 1, current_sum + numbers[index])
        # 현재 숫자를 빼는 경우
        minus = dfs(index + 1, current_sum - numbers[index])
        
        return plus + minus

    return dfs(0, 0)