from collections import deque

t = int(input())
n = int(input())

for _ in range(t):
    s_x, s_y = map(int, input().split())
    conv = []
    for _ in range(n):
        c_x, c_y = map(int, input().split())
        conv.append([c_x, c_y])
    f_x, f_y = map(int, input().split())

    #1 시작지점과 편의점지점이 거리 안에 있드면 끝!
    if abs(s_x - f_x) + abs(s_y - f_y) <= 1000:
        print("happy")
        return

    #2 거리 안에 없다면?
    