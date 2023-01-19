n, l = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

def check(line):
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1:
            return False
        if line[i] < line[i - 1]:
            for j in range(l):
                if i + j >= n or line[i] != line[i + j] or slope[i + j]:
                    return False
                if line[i] == line[i + j]:
                    slope[i + j] = True
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False
                if line[i - 1] == line[i - j - 1]:
                    slope[i - j - 1] = True
    return True

result = 0
for i in range(n):
    slope = [False] * n
    if check([data[i][j] for j in range(n)]):
        result += 1
for j in range(n):
    slope = [False] * n
    if check([data[i][j] for i in range(n)]):
        result += 1
print(result)



