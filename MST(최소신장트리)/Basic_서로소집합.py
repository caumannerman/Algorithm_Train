import sys
input = sys.stdin.readline

n, m = map(int, input().split())# 노드 갯수, 합집합 연산 갯수
parent = [i for  i in range(n+1)]

def find(parent, v):
    if parent[v] != v:
        parent[v]  = find(parent, parent[v])
    return parent[v]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a, b = map(int, input().split())
    union(parent, a,b)

# 마지막에 find 한 번 씩 돌려서 해야한다.
for i in range(1, n+1):
    find(parent, i)
print( * parent[1:])

