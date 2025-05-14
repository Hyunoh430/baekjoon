from collections import deque

def solution(board):
    N = len(board)
    M = len(board[0])
    visited = [[-1] * M for _ in range(N)]
    #print(visited)
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    q = deque()
    for i in range(N):
        for j in range(M):
            if(board[i][j] == 'R'):
                q.append([i, j])
                visited[i][j] = 0
    
    while q:
        x,y = q.popleft()
        distance = visited[x][y]
        if board[x][y] == 'G':
            return distance
        for i in range(4):
            nx, ny = x, y
            
            while(True):
                nx, ny = nx + dx[i], ny + dy[i]
                
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    nx, ny = nx - dx[i], ny - dy[i]
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = distance + 1
                        q.append([nx,ny])
                    break
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 'D':
                    nx, ny = nx - dx[i], ny - dy[i]
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = distance + 1
                        q.append([nx, ny])
                    break
                
    return -1
                                                    
              
    answer = 0
    return answer