# 그래프 이론에서 사용했던 """서로소 집합""" 을 이용하여, 무방향 그래프에서의 싸이클 유무 판별 소스코드를 작성하였다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(parent, x, y):
    a = parent[x]
    b = parent[y]

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0]*(v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        print("싸이클 발생")
        break
    else:
        union(parent, a, b)

print("싸이클 없음")