"""벨만-포드 알고리즘
- '음의 간선'이 있을 때,   시작점으로부터 모든 점까지 최단거리 구할 수 있음
 ( 일반화 된 다익스트라 느낌 )
 ** 음의 간선 싸이클이 있는 경우, 모든 점까지 -무한대 거리로 도달할 수 있음 주의
  BF알고리즘은 음의 간선 싸이클을 탐지할 수 있다.
  """


import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
data = [] # 간선정보 담을 리스트
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    data.append((a,b,c))
# n-1번 edge relaxation 하고 나면 더이상 update가 일어나지 않아야 정상임....
# n 번째에 relaxation에서 update가 일어난다는 것은 "음의 싸이클" 이 존재한다는 것이다.

def bf(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            cur = data[j][0]
            next = data[j][1]
            cost = data[j][2]
            if distance[cur] != INF and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == n-1:
                    return True
    return False

negative = bf(1)

if negative:
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])