''' 온라인으로 컴공 강의를 듣고있다. 이때 각 온라인 강의는 선수강의가 있을 수 있는데, 선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있따.
예를 들어, '알고리즘' 강의의 선수 강의로 '자료구조'와 '컴퓨터 기초' 가 존재하면, 둘 다 들은 후 '알고리즘' 을 들을 수 있다.

주인공은 총 N개의 강의를 듣고자 한다.  강의는 1번부터 N번 까지의 번호를 가진다. 예를 들어 N = 3일 때,
3번 강의의 선수 강의로 1번과 2번 강의가 있고, 1,2번강의는 선수강의가 없다고 가정하자.각 그리고 각 강의에 대하여 강의 시간이 다음과 같다고 가정하자

   1번 강의 : 30시간
   2번 강의 : 20시간
   3번 강의 : 40시간

   이 경우 1번강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지의 최소시간은 20시간, 3번강의를 수강하기까지 최소시간은 60시간이다.'''

# 첫째 줄에 듣고자하는 강의의 수 N ( 1<= N <= 500 ) 이 주어진다
# 다음 N개의 줄에 각 강의의 강의시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분된다. 이 때 강의시간은 100,000 이하의 자연수다.
# 각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.의
# 출력 - N개의 강의에 대하여 수강하기까지 걸리는 최소시간을 한 줄에 하나씩 출력한다.
from collections import deque
from collections import deque
import copy

import sys
from collections import deque
import copy
input = sys.stdin.readline
n = int(input())

# topology 기본 indegree(진입차수), graph
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)


for i in range(1,n+1):
    now = list(map(int, input().split()))
    time[i] = now[0]
# 여기서 조심해야할 것이, j에서 i로 진입경로가 존재한다면, graph[j]에 i를 append해줘야한다. ==> q에서 j를 꺼냈을 때, q에서 갈 수 있는 노드들에 대해 indegree를 빼줘야하므로.
    for j in now[1:-1]:
        graph[j].append(i)
    indegree[i] += len(now) - 2


def topology():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
# 이것이 핵심 알고리즘. 이미 다른 선수과목에서 해당 과목까지 걸리는 시간을 초기화했을 수 있으므로,  max로 처리. 그랬든 안 그랬든 indegree는 줄여줘야한다.
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result[1:]:
        print(i)

topology()