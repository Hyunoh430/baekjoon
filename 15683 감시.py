n, m = map(int, input().split())
board = []
cctvs = []

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j], i, j))

# 방향: 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV별 가능한 방향 조합
directions = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}


def watch(board, x, y, dirs):
    for d in dirs:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = 7


def count_zero(board):
    count = 0
    for row in board:
        count += row.count(0)
    return count


def solve(idx, board):
    if idx == len(cctvs):
        return count_zero(board)

    cctv_type, x, y = cctvs[idx]
    min_blind_spots = 99999

    for dirs in directions[cctv_type]:
        # 보드 복사
        new_board = [row[:] for row in board]
        # 감시
        watch(new_board, x, y, dirs)
        # 다음 CCTV로 넘어가서 사각지대 개수 받아오기
        blind_spots = solve(idx + 1, new_board)
        # 지금까지 중에서 가장 적은 사각지대 개수 저장
        if blind_spots < min_blind_spots:
            min_blind_spots = blind_spots

    return min_blind_spots


print(solve(0, board))