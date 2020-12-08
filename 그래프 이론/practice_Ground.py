#12.9 Disjoint Set
'''
v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1,v+1):
    parent[i] = i

def find_parent(v):
    if parent[v] != v:
        parent[v] = find_parent(parent[v])
    return parent[v]

def union(x,y):
    a = find_parent(x)
    b = find_parent(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(e):
    a, b = map(int, input().split())
    union(a, b)



print(parent[1:])

for i in range(1, v+1):
    print(find_parent(i), end = ' ')
print()
print(parent[1:])
'''

#12.9 Kruskal Algorithm
# 신장트리. 싸이클 없어야 함. 최소 비용 구하기.

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

v, e = map(int, input().split())
parent = [0]*(v+1)
cost = 0
graph = []
for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b, c = map(int, input().split())
    graph.append((c,a,b))

graph = sorted(graph)

for i in graph:
    if find_parent(parent, i[1]) != find_parent(parent, i[2]):
        cost += i[0]
        union(parent, i[1], i[2])
    else:
        continue

print(cost)

