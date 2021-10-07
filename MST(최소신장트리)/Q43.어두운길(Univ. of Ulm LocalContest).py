"""한 마을은 N개의 집과 M개의 도로로 구성되어 있습니다. 각 집은 0번부터 N-1번까지의 번호로 구분됩니다. 모든 도로에는 가로등이 구비되어있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은
해당 도로의 길이와 동일합니다. 예를 들어 2번 집과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 해봅시다. 하루동안 이 가로등을르 켜기 위하 비용은 7이 됩니다.
정부에서는 일부 가로등르 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오락ㄹ 수 있도록 만들고자 합니다. 결과적으로 일부 가로등을 비활성화하여
최대한 많은 금액을 절약하고자 합니다. 마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하시오"""
# 입력 : 첮 째 줄에 집의 수 N과 도로의 수 M이 주어진다.
# 다음 M개의 줄에 걸쳐서 각 도로에 대한 정보 X,Y,Z가 주어지며, 공백으로 구분한다. X,Y,Z는 X번 집과 Y번 집 사이에 양방향 도로가 있으며, 그 길이가 Z라는 말이다.
# X,Y가 같은 경우는 없다
# 출력 : 첫 째 줄에 일부 가로등을 비활성화하여 절약할 수 있는 최대금액을 출력한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
total = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    data.append((z,x,y))
    total += z

parent = [i for i in range(n+1)]

def find(parent,v):
    if parent[v] != v:
        parent[v] = find(parent,parent[v])
    return parent[v]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

data.sort()
count = 0
for cost, x,y in data:
    if find(parent, x) == find(parent, y):
        continue
    else:
        union(parent, x, y)
        count += cost

print(total - count)