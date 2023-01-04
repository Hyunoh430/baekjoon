m, n = map(int, input().split())
graph = [[0] * m for _ in range(n)]
count = int(input())
store = []
for i in range(count + 1):
    x, y = map(int, input().split())
    if x == 1:
        store.append([0, y])
    elif x == 2:
        store.append([n, y])
    elif x == 3:
        store.append([y, 0])
    elif x == 4:
        store.append([y, m])         #store[count]는 동근이의 위치
#print(store)
distance = 0
for i in range(count):
    if (abs(store[count][0] - store[i][0]) == n) or (abs(store[count][1] - store[i][1]) == m):
        if abs(store[count][0] - store[i][0]) == n:
            distance1 = store[count][1] + store[i][1] + n
            distance2 = (m - store[count][1]) + (m - store[i][1]) + n
            distance += min(distance1, distance2)
        elif abs(store[count][1] - store[i][1]) == m:
            distance1 = store[count][0] + store[i][0] + m
            distance2 = (n - store[count][0]) + (n - store[i][0]) + m
            distance += min(distance1, distance2)
        #print(11111)
    else:
        distance += (abs(store[count][0] - store[i][0]) + abs(store[count][1] - store[i][1]))
        #print(2222)
print(distance)