#전형적인 heapq를 사용한 Greedy

""" data를 먼저 list에 받아  '정렬'하고 하나씩 접근해 heapq에 담으며 연산하는 것이 핵심 """
import sys

input = sys.stdin.readline
import heapq

n = int(input())
data = []
result = 1

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort()

q = [0]

for i in range(n):
    if q[0] <= data[i][0]:
        heapq.heappop(q)
        heapq.heappush(q, data[i][1])
    else:
        heapq.heappush(q, data[i][1])
print(len(q))