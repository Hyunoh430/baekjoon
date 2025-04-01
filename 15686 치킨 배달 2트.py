from itertools import combinations

N, M = map(int, input().split())
city = []
chicken = []
house = []

for i in range(N):
    city.append(list(map(int, input().split())))
    for j in range(N):
        if city[i][j] == 1:
            house.append([i,j])
        elif city[i][j] == 2:
            chicken.append([i,j])

chicken_list = list(combinations(chicken, M))
#print(chicken_list)

def distance(chicken, house):
    dis = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
    return dis


min_value = float('inf')
for chicken in chicken_list:
#치킨 집 후보들을 다 둘러보자 ㅇㅇ
    chicken_distance = []
    for h in house: #치킨 집 후보들 중 하나하나 씩 들어가보자
        min_h = []
        for c in chicken: #집과 치킨의 거리를 구해보자 (치킨거리 후보)
            min_h.append(distance(c,h))
        #print(min_h)
        chicken_distance.append(min(min_h))   # 치킨거리 후보 중 제일 작은 값을
    if min_value > sum(chicken_distance) :
        min_value = sum(chicken_distance)

print(min_value)

