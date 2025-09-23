from collections import deque

t = int(input())


for _ in range(t):
    n = int(input())
    s_x, s_y = map(int, input().split())
    conv = []
    for _ in range(n):
        c_x, c_y = map(int, input().split())
        conv.append([c_x, c_y])
    f_x, f_y = map(int, input().split())

    #1 시작지점과 편의점지점이 거리 안에 있드면 끝!
    if abs(s_x - f_x) + abs(s_y - f_y) <= 1000:
        print("happy")
        break

    #2 거리 안에 없다면? 편의점 있나 확인
    q = deque()
    q.append([s_x, s_y])
    check = 0
    while q:
        x, y = q.popleft()
        if abs(x - f_x) + abs(y - f_y) <= 1000:
            check = 1
            print("happy")
            break
        for i in range(n):
            new_x, new_y = conv[i]
            if abs(x - new_x) + abs(y - new_y) <= 1000:
                q.append([new_x, new_y])
    if check == 1:
        print("sad")


