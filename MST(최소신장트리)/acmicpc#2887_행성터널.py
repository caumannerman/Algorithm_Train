"""때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다.
 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.

행성은 3차원 좌표위의 한 점으로 생각하면 된다.
 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오."""

# 입력 : 첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다.
# 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다.
# 출력 : 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.
import sys
input = sys.stdin.readline

n = int(input())
data_x= []
data_y = []
data_z = []

parent = [i for i in range( n +1)]

for i in range(1 , n +1):
    x ,y ,z = map(int, input().split())
    data_x.append((x ,i))
    data_y.append((y ,i))
    data_z.append((z ,i))

def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent ,parent[v])
    return parent[v]
def union(parent, a ,b):
    a = find(parent, a)
    b = find(parent ,b )
    if a< b:
        parent[b] = a
    else:
        parent[a] = b


data_x.sort()
data_y.sort()
data_z.sort()
distance = []

for i in range(1, n):
    distance.append((abs(data_x[i][0] - data_x[i - 1][0]), data_x[i][1], data_x[i - 1][1]))
    distance.append((abs(data_y[i][0] - data_y[i - 1][0]), data_y[i][1], data_y[i - 1][1]))
    distance.append((abs(data_z[i][0] - data_z[i - 1][0]), data_z[i][1], data_z[i - 1][1]))

distance.sort()
result = 0
for cost, x, y in distance:
    if find(parent, x) == find(parent, y):
        continue
    else:
        union(parent, x, y)
        result += cost
print(result)