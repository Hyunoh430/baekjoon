N, M, H = map(int, input().split())
ladder = [[False] * (N + 1) for _ in range(H + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = True


def check():
    for i in range(1, N + 1):
        pos = i
        for level in range(1, H + 1):
            if pos < N and ladder[level][pos]:
                pos += 1
            elif pos > 1 and ladder[level][pos - 1]:
                pos -= 1

        if pos != i:
            return False

    return True


def dfs(level, pos, cnt, target):

    if cnt == target:
        return check()
    if check():
        return True
    for i in range(level, H + 1):
        start = pos if i == level else 1
        for j in range(start, N):
            can_install = True
            if ladder[i][j]:
                can_install = False
            elif j > 1 and ladder[i][j - 1]:
                can_install = False
            elif j < N - 1 and ladder[i][j + 1]:
                can_install = False

            if can_install:
                ladder[i][j] = True
                if dfs(i, j + 1, cnt + 1, target):
                    return True
                ladder[i][j] = False
        pos = 1

    return False

if check():
    print(0)
else:
    answer = -1
    for target in range(4):
        if dfs(1, 1, 0, target):
            answer = target
            break

print(answer)