"""수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오."""
# 입력 : 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# 출력 : 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.


""" visited가 bfs의 회전 수를 나타내주는 용도로 쓰일 수 있음을 알려주는 대표적인 문제.
우리가 게임 관련 문제를 bfs로 해결하며, map data 위를 이동하며 0이었던 칸들을 1,2,3, 등으로 바꿔가고, 도착 칸의 내용물을 이동횟수로서 정답을 낸 적이 있다.
이와 같은 개념을 2차원 배열과 dx, dy를 쓰는 대신 0으로 이루어져 시작하는 visited 리스트 하나로 구현할 수 있다."""
from collections import deque

n, k = map(int, input().split())
# 이와 같이 LIMIT을 const화 해주고 아래의 알고리즘에서 사용하는 것이 깔끔하다.
LIMIT = 100001
visited = [0] * LIMIT


def bfs(n, k):
    q = deque([n])

    while q:
        a = q.popleft()
        if a == k:
            return visited[a]
        for j in (a + 1, a - 1, a * 2):
            if (0 <= j < LIMIT) and not visited[j]:
                visited[j] = visited[a] + 1
                q.append(j)


print(bfs(n, k))