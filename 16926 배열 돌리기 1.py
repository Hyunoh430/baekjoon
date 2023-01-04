n, m, r = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

def rotate():
    for i in range(min(n, m) // 2):
        tmp = data[i][i]
        for j in range(i + 1, n - i):       #하 방향
            tmp2 = data[j][i]
            data[j][i] = tmp
            tmp = tmp2

        for j in range(i + 1, m - i):        #우 방향
            tmp2 = data[n - i - 1][j]
            data[n - i - 1][j] = tmp
            tmp = tmp2

        for j in range(n - i - 2, i-1, -1):  #상 방향
            tmp2 = data[j][m - i - 1]
            data[j][m - i - 1] = tmp
            tmp = tmp2

        for j in range(m - i - 2, i-1, -1):      #좌 방향
            tmp2 = data[i][j]
            data[i][j] = tmp
            tmp = tmp2
for _ in range(r):
    rotate()
for i in range(n):
    for j in range(m):
        print(data[i][j], end = ' ')
    print()


