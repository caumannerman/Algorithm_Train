"""수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오."""
# 입력 : 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 출력 : 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

import heapq

INF = int(1e9)
n, k = map(int, input().split())
distance = [INF] * (100001)


def dijkstra(start):
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
################################ 매우 중요!!!  처음 코딩했을 때, 조금이나마 빨리 발견하려고 함수 마지막 부분에서 i ==k 인 것이 처음 나오면, cost를 return했다.
# 그랬을 경우 잘못된 , 즉  k까지 가는 최소 비용보다 큰 값이 나올 수 있다.
        if now == k:
            return dist
        c = 0
        for i in (now - 1, now + 1, now * 2):
            c += 1
            if 0 <= i <= 100000:
                if c != 3:
                    cost = dist + 1
                else:
                    cost = dist
                if distance[i] > cost:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))


if n == k:
    print(0)
    exit()
else:
    print(dijkstra(n))