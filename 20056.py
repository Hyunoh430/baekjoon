N, M, K = map(int, input().split())
#r,c 위치, 질량 m, 방향 d, 속력 s
balls = []
board = [[[] for _ in range(N)]for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]



for i in range(M):
    r, c, m, s, d = map(int, input().split())
    balls.append([r - 1,c - 1,m,s,d])

for _ in range(K):
    board = [[[] for _ in range(N)] for _ in range(N)]
    while balls:
        r, c, m, s, d = balls.pop()
        nr = (r + dx[d] * s) % N
        nc = (c + dy[d] * s) % N
        board[nr][nc].append([m,s,d])

    for r in range(N):
        for c in range(N):
            if len(board[r][c]) == 1:
                m, s, d = board[r][c][0]
                balls.append([r,c,m,s,d])
            elif len(board[r][c]) > 1:
                total_m = sum(fb[0] for fb in board[r][c])
                total_s = sum(fb[1] for fb in board[r][c])
                count = len(board[r][c])

                new_m = total_m // 5
                new_s = total_s // count
                if new_m == 0:
                    continue

                directions = [fb[2] for fb in board[r][c]]
                if all(d % 2 == 0 for d in directions) or all(d % 2 == 1 for d in directions):
                    new_dirs = [0, 2, 4, 6]
                else:
                    new_dirs = [1, 3, 5, 7]

                for new_d in new_dirs:
                    balls.append([r,c,new_m, new_s, new_d])


print(sum(ball[2] for ball in balls))

