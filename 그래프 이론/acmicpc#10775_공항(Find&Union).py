"""오늘은 신승원의 생일이다.

박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다.
비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?"""
# 입력 : 첫 번째 줄에는 게이트의 수 G (1 ≤ G ≤ 105)가 주어진다.
#
# 두 번째 줄에는 비행기의 수 P (1 ≤ P ≤ 105)가 주어진다.
#
# 이후 P개의 줄에 gi (1 ≤ gi ≤ G) 가 주어진다.
# 출력 : 승원이가 도킹시킬 수 있는 최대의 비행기 수를 출력한다.

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


g = int(input())
p = int(input())
data = []
parent = list(range(0, g + 1))
result = 0
for _ in range(p):
    now = int(input())
    now_parent = find_parent(parent, now)
    if now_parent == 0:
        print(result)
        exit()
    else:
# 이곳에서 , union을 해줄 때, now 게이트를 union시켜주는 것이 아니라, now의 parent와 그 직전 게이트를 union해주어야,
# now_parent 뒤의 모든 게이트들도 한번에 적용이 되는 것이 포인트!!!!!!!!!
        union(parent, now_parent, now_parent - 1)
        result += 1
print(result)