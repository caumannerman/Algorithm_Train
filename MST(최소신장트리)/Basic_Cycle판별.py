import sys
input = sys.stdin.readline

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
n ,m = map(int, input().split())
parent = [i for i in range(n+1)]

cycle = False
for i in range(m):
    a, b = map(int, input().split())

    if find(parent, a) == find(parent, b):
        cycle = True
        break
    else:
        union(parent, a, b)

if cycle:
    print("cycle 발생")
else:
    print("cycle 없음")
