from collections import deque
n, w, l = map(int, input().split())
data = list(map(int, input().split()))
cars = deque(data)

bridge = deque()
trucks_time = [0] * n
i = 0
time = 0
while True:
    time += 1
    if len(cars) != 0:
        if cars[0] + sum(bridge) <= l and len(bridge) + 1 <= w:
            bridge.append(cars.popleft())
            i += 1

    for j in range(i):
        trucks_time[j] += 1
        if trucks_time[j] > w:
            continue
        if trucks_time[j] == w:
            bridge.popleft()
    if len(cars) == 0 and len(bridge) == 0:
        break
print(time + 1)
