"""최소 스패닝 트리(MST)는 '무방향 그래프'에서 사용 가능 """
# 1. find&union은 그대로 작성
# 2. 간선입력을 받으며, (cost, a, b) 순서로 입력
# 3. sort()
# 4. cycle이 생기지 않는 한 계속 union

def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n ,m = map(int, input().split())
parent = [i for i in range(n+1)]

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
result = 0
for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
    else:
        continue

print(result)