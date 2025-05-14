from collections import deque
#체스판을 벗어나는 경우에도 파란색 처럼 취급

N, K = map(int, input().split())
graph = []
horse = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))       #빨간색인지, 파란색인지 위치정보 저장
h_info = []
for i in range(K):
    x, y, d = map(int, input().split())
    h_info.append([x-1, y-1, d-1])      #말 정보 저장, (r,c 방향)
    horse[x-1][y-1].append(i)  #인덱스와 말 정보 전달


dx = [0,0,-1,1]
dy = [1,-1,0,0]




#print(h_info)
c = 0
while(c <= 1000):
    c+=1

    for h in h_info:

        x, y, d = h

        nx = x + dx[d]
        ny = y + dy[d]

        if graph[nx][ny] == 1:      #빨간색인 경우
            add_list = reversed(horse[x][y])
            horse[nx][ny].append(add_list)     #몇번말이다 알려주면서 위에 올림

        elif graph[nx][ny] == 2:    #파란색인 경우






