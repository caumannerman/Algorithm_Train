'''동물원에서 막 탈출한 원숭이 한 마리가 세상 구경을 하고있다. 어느 날 원숭이는 '평화로운 마을'에 잠시 머물렀는데 마침 마을 사람들은 도로공사 문제로 머리를 맞대고 회의중이었다.

 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다. 그리고 길마다 길을 유지하는데 드는 유지비가 있다.

 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.  마을을 분할할 때, 각 분리된 마을 안의 집들이 서로 연결되도록 분할해야한다.
  즉, 분리된 마을 안에 있는 임의의 두 집 사이에, 경로가 항상 존재해야한다는 뜻이다.
  + 마을에는 집이 하나 이상 있어야 한다.

  길들은 유지비가 있으므로, 일단 분리된 두 마을 사이의 길들은 없앨 수 있고, 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다.

      ' 마을의 이장은, 위 조건을 만족하도록 길들을 모두 없애고, 나머지 길의 유지비의 합을 최소로 하고싶다. 이를 구하는 프로그램을 구하시오.'''
# 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2 이상 100,000 이하인 정수, M은 1이상 1,000,000 이하인 정수이다.
# 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A,B,C 3개의 정수로 공백을 두고 구분되어 주어지는데, A번 집과 B번 집을 연결하는 길의 유지비가 C( 1~1000 사이) 라는 뜻이다.
# 출력 - 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력하라



# 크루스칼 이용
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b



n, m = map(int, input().split())
parent = [x for x in range(n+1)]
edge = []

for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((c,a,b))

edge = sorted(edge)
result = 0

for i in edge:
    if find_parent(parent,i[1]) != find_parent(parent, i[2]):
        union(parent, i[1], i[2])
        result += i[0]
        last = i[0]

print(result - last)