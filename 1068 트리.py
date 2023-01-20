n = int(input())
data = [[] for _ in range(n)]
a = list(map(int, input().split()))
erase = int(input())
for i in range(n):
    if a[i] == -1:
        continue
    data[a[i]].append(i)
visited = [False] * n
#print(data)
def dfs(erase):
    visited[erase] = True
    for i in data[erase]:
        if not visited[i]:
            dfs(i)
dfs(erase)
for i in range(n):
    if visited[i]:
        for j in range(n):
            for num in data[j]:
                if num == i:
                    data[j].remove(num)

cnt = 0
for i in range(n):
    if len(data[i]) == 0:
        if not visited[i]:
            cnt += 1
print(cnt)




