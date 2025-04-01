from itertools import combinations

n, m = map(int, input().split())
cities = []
house = []
chicken = []
for i in range(n):
    cities.append(list(map(int, input().split())))
    for j in range(n):
        if cities[i][j] == 1:
            house.append([i, j])        #집 위치 입력
        elif cities[i][j] == 2:
            chicken.append([i, j])      #치킨 집 위치 입력

#치킨집 M개 골라보자
chicken_list = list(combinations(chicken, m))
def distance(chicken, house):          #치킨집과 집의 거리 구하기 함수
    result = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
    return result

roadlen = []       #집과 치킨집 거리
chicken_distance = []           #치킨 거리
city_distance = []              #도시의 치킨 거리
for i in range(len(chicken_list)):          #치킨 집 m개 골랐을때 모든 경우의 수 따지기
    for j in range(len(house)):
        for chick in chicken_list[i]:               #combination으로 뽑은 경우 하나씩 비교
            roadlen.append(distance(chick, house[j]))           #집과 치킨집의 거리 모두 추가
        chicken_distance.append(min(roadlen))       #거리 중 제일 작은 값 치킨 거리 목록에 추가
        roadlen = []
    city_distance.append(sum(chicken_distance))
    chicken_distance = []

print(min(city_distance))





