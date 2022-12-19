n, m = map(int, input().split())
j = int(input())
apple = []
for i in range(j):
    apple.append(int(input()))

start = 1
end = m
distance = 0
for i in range(j):
    if start <= apple[i] <= end:
        continue
    elif end < apple[i]:
        distance += apple[i] - end
        end = apple[i]
        start = end - m + 1
    elif apple[i] < start:
        distance += start - apple[i]
        start = apple[i]
        end = start + m - 1

print(distance)