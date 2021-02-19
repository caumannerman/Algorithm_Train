
from collections import deque
n, k = map(int, input().split())
LIMIT = 100001
visited = [False] * LIMIT

if n== k:
    print(0)
    exit()


def bfs(n, k):
    q = deque([(n, 0)])
    visited[n] = True
    while q:
        a, count = q.popleft()
        for j in (a + 1, a - 1, a * 2):
            if (0 <= j < LIMIT) and not visited[j]:

                visited[j] = True
                q.append((j, count + 1))
                if j == k:
                    return count + 1


print(bfs(n, k))