from collections import deque
data = []
for i in range(4):
    data.append(list(map(int, input())))
k = int(input())

for _ in range(k):
    num, direction = map(int, input().split())
    rotation = [0, 0, 0, 0]
    rotation[num - 1] = direction
    for i in range(num, 4):
        if data[i][6] != data[i - 1][2]:
            rotation[i] = -rotation[i - 1]
        else:
            break
    for i in range(num - 2, -1, -1):
        if data[i][2] != data[i + 1][6]:
            rotation[i] = -rotation[i + 1]
        else:
            break
    for i in range(4):
        q = deque(data[i])
        q.rotate(rotation[i])
        data[i] = list(q)


result = 0
score = 1
for i in range(4):
    if data[i][0] == 1:
        result += score
    score *= 2
print(result)

