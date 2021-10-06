import sys
input = sys.stdin.readline

def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent, parent[v])
    return parent[v]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b


n ,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(set(map(int, input().split())))
parent = [i for i in range(n+1)]

for i in range(n-1):
    for j in range(i+1,n):
        if graph[i][j] == 1:
            union(parent,i,j)
result_p = find(parent, plan[0])

for i in plan[1:]:
    if find(parent,i) != result_p:
        print("NO")
print("YES")

