n = int(input())
number = int(input())
data = list(map(int, input().split()))
score = dict()
result = []

for num in data:
    if num in result:
        score[num] += 1
        continue
    if len(result) == n :
        minnum = 1e9
        count = -1
        if num not in result:
            for i in result:
                minnum = min(minnum, score[i])
            for i in result:
                count += 1
                if minnum == score[i]:
                    score[i] = 0
                    result.pop(count)
                    result.append(num)
                    score[num] = 1
                    break

        continue

    result.append(num)
    score[num] = 1
result.sort()
for num in result:
    print(num, end = ' ')


