#12.9 Disjoint Set

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