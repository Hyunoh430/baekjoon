from collections import deque
n, m = map(int, input().split())
board = [0] * 101
visited = [False] * 101
ladders = dict()
snakes = dict()
for i in range(n):
    a, b = map(int, input().split())
    ladders[a] = (b)
for i in range(m):
    a, b = map(int, input().split())
    snakes[a] = b


q = deque()
q.append(1)
visited[1] = True
while q:
    now = q.popleft()
    for i in range(1, 7):
        next = now + i
        if next <= 100 and (visited[next] == False):
            if next in ladders:
                next = ladders[next]
            if next in snakes:
                next = snakes[next]
            if visited[next] == False:
                q.append(next)
                visited[next] = True
                board[next] = board[now] + 1

print(board[100])
