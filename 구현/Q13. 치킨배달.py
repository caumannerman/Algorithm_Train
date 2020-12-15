""" 크기가 NxN인 도시가 있다. 도시는 1x1 크기의 칸으로 나뉘었고, 도시의 각 칸은 빈칸, 치킨집, 집 중 하나다.
도시의 칸은 (r, c)와 같이 나타내고, r행 c열 또는 위에서부터 r번 째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서 사람들은 "치킨거리" 라는 말을 주로 사용한다. 치킨거리는 집과 가장 가까운 치킨집 사이의 거리이다.
즉, 치킨거리는 집을 기준으로 정해지며, 각각의 집은 치킨거리를 가지고 있다. 도시의 치킨거리는 모든 집의 치킨 거리의 합이다.

임의의 두 칸 (r1,c1) 과 (r2,c2)사이의 거리는 |r1-r2| + |c1-c2| 로 구한다.

이 도시에 있는 치킨집은 모두 같은 프랜차이즈이다. 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개라는 사실을 알아냈다.
도시에 있는 치킨집 중 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하라.
"""
# 첫 째 줄에 N(2~50) 과 M(1~13)이 주어진다.
# 둘 째 줄부터 N개의 줄에는 도시의 정보가 주어진다.
# 도시으 ㅣ정보는 0,1,2로 이로어져있고, 차례로 빈칸,집,치킨집을 의미한다. 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재한다.
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같다
# 출력 - 첫 째 줄에 폐업시키지 않을 치킨집을 최대 M개 골랐을 때 도시의 치킨 거리의 최솟값을

from itertools import combinations


def distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


n, m = map(int,input().split())

city = []
chicken = []
house = []

for _ in range(n):
    temp = list(map(int, input().split()))
    city.append(temp)


for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))
        if city[i][j] == 1:
            house.append((i,j))

choose_m = list(combinations(chicken,m))

result = []
for i in choose_m:
    chick_distance = 0
    for h in house:
        min_one = 100
        for j in i:
            if distance(h,j) < min_one:
                min_one = distance(h,j)
        chick_distance += min_one

    result.append(chick_distance)

print(min(result))

