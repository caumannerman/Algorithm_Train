"""공항에 G개의 탑승구가 있으며, 각각의 탑승구는 1번부터 G번까지의 번호로 구분됨
공항에는 p개의 비행기가 차례로 도착할 예정이며, i번째 비행기를 1번부터 gi 번 째 탑승구 중 하나에 영구적으로 도킹해야한다.
이 때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있다.
또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서 공항의 운행을 중지한다.
공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 한다.
비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하라."""

# 첫 째 줄에는 탑승구의 수 G가 주어진다. 100,000 이하
# 둘 째 줄에는 비행기의 수 P가 주어진다 100,000 이하
# 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 gi가 주어진다.
# 이는 i번째 비행기가 1번부터 gi번째 탑승구 중 하나에 도킹할 수 있다는 의미이다.


import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

data = []
for _ in range(p):
    data.append(int(input()))

def find(parent, v):
    if parent[v] != v:
        parent[v] = find(parent,parent[v])
    return parent[v]
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(g+1)]
count = 0
for i in data:
    now_p = find(parent, i)
    if now_p != 0:
        union(parent, now_p,now_p - 1)
        count += 1
    else:
        print(count)
        exit()

