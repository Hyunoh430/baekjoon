N = int(input())
students = []
for _ in range(N**2):
    students.append(list(map(int, input().split())))

data = [[0] * N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for student in students:
    result = []
    for i in range(N):
        for j in range(N):
            prefer1 = 0
            prefer2 = 0
            if data[i][j] == 0: # 빈 자리가 있다면?
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if (data[nx][ny] in student[1:]):
                           prefer1 += 1     #인접 칸에 좋아하는 학생 얼마나 있나
                        if (data[nx][ny] == 0):
                            prefer2 += 1    #인접 칸에 비어있는 칸 몇개 인가
                result.append((prefer1, prefer2, i, j))
    result.sort(key = lambda x: (-x[0], -x[1], x[2], x[3])) #1번,2번 기준 후 행 번호 작은거 그 후 열 번호 가장 작은거
    data[result[0][2]][result[0][3]] = student[0]

def search(x):
    for i in range(N ** 2):
        if students[i][0] == x:
            #print(students[i][1:])
            #print(x)
            #print(1111)
            return i

score = [0,1,10,100,1000]
result = 0
for i in range(N):
    for j in range(N):
        check = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                num = search(data[i][j])
                if data[nx][ny] in students[num][1:]:
                    check += 1
        result += score[check]

print(result)