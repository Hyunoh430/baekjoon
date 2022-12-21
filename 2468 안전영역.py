import sys
sys.setrecursionlimit(10**6)
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
array = [[1] * n for _ in range(n)]


maxnum = max(map(max, data))

standards = []
#기준이 maxnum이나 minnum일 경우 안전영역이 1이므로 각각 -1, +1로 부터 기준설정
for i in range(0, maxnum + 1):
    standards.append(i)

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    if array[x][y] == 1:
        array[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
answer = []
for standard in standards:
    array = [[1] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] <= standard:
                array[i][j] = 0             #잠기는 지역은 0으로 표시

    for i in range(n):
        for j in range(n):
            if array[i][j] == 1:
                dfs(i, j)
                result += 1
    answer.append(result)

print(max(answer))


