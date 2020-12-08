"""크루스칼 알고리즘  ( 최소 신장트리 알고리즘 중   하나 )  -- ( 신장 트리 : 모든 노드 포함하며 사이클이 존재X )
        '최소한의 비용' -> 신장 트리 찾기 ( 가장 적은 비용으로 모든 노드를 연결 )
        + 크루스칼 알고리즘은 Greedy 알고리즘으로 분류됨 """

# 1. 간선 데이터를 비용에 따라 오름차순 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
#       - 사이클이 발생하지 않으면 최소 신장 트리에 포함시킴
#       - 사이클이 발생하는 경우, 최소 신장트리에 포함하지 않음
# 3. 모든 간선에 대하여 2번 과정을 반복
''' 이렇게 하면 최적의 해 보장!'''



def find_p(parent, v):
    if parent[v] != v:
        parent[v] = find_p(parent, parent[v])
    return parent[v]

def union_parent(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, e = map(int, input().split())
parent = [0]*(n+1)
edge = []
result = 0

for i in range(1, n + 1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c,a,b))

edge.sort()

for eg in edge:
    cost, a, b = eg

    if find_p(parent, a) != find_p(parent, b):
        union_parent(parent, a, b)
        result += cost



print(result)

