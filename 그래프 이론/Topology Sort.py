""" 위상정렬은 순서가 정해져있는 일련의 작업을 차례로 수행해야 할 때 사용할 수 있는 알고리즘.
          ( 방향 그래프의 모든 노드를 '방향성에 거스르지 않도록 순서대로 나열하는 것' )
        사용 예시 -> 커리큘럼 선수과목


위상정렬 알고리즘
1. 진입차수(들어오는 간선의 수)가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음을 반복
    - 큐에서 원소를 꺼내, 해당 노드에서 출발하는 간선을 (모두) 그래프에서 제거한다.
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

    * 큐에서 원소가 V번 추출되기 전에 큐가 비면, '사이클'이 발생한 것이다 """


from collections import deque

v, e = map(int, input().split())

# 진입차수
indegree = [0]*(v+1)
graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


#Topology Sort 함수

def tplgy_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end= ' ')


#실행
tplgy_sort()