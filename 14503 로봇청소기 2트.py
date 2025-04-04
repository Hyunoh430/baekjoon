N, M = map(int, input().split())
x, y, direction = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))


# 청소되지 않은게 있다면? 반시계

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]  #북, 동, 남, 서 (index 번호에 맞게) index - 1해주면 반시계 보게 됨


check = 0   #방향을 몇번 돌앗나 확인하기 위함
result = 0
#1이 벽, 0이 청소되지 않음, 2가 청소된걸로 하자 걍
while(1):
    if(graph[x][y] == 0):   #현재 칸이 청소가 안됐다면 청소해라
        graph[x][y] = 2
        result += 1
        print()
        for i in range(N):
            print(graph[i])

    direction = direction - 1   # 일단 반시계 회전 한번 하자
    if direction == -1:
        direction = 3

    nx = x + dx[direction]  #다음 위치 정보
    ny = y + dy[direction]

    if graph[nx][ny] == 1 or graph[nx][ny] == 2: #청소가 됐거나 벽이면?
        if (check == 4):        #결국 4 방향 다 확인해보고 하나가 더 돌아갔으니깐
            nx = x - dx[direction]
            ny = y - dy[direction]
            if graph[nx][ny] == 1:  #만약 뒤로 갔는데 벽이면 걍 종료
                break
            else:
                x, y = nx, ny
                check = 0
                continue
        check += 1
        continue

    elif graph[nx][ny] == 0:  #청소가 안됐으면? 가서 청소하고 처음으로 돌아감
        check = 0
        x, y = nx, ny
        continue

print(result)

