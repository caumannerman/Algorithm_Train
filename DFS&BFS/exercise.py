''':keyword

STACK
QUEUE ( DEQUE )
RECURSIVE FUNCTION

'''

# list와 append(), pop()을 이용해 스택기능 다 쓸 수 있다.
# dfs, bfs 는 stack과 queue를 많이 씀. 출제도 많이 하므로 잘 알아둬야함.

#from collections import deque 해주면 덱 -> 스택, 큐 기능 모두 있ㄴ는놈!!!
# stack은 그냥 리스트 쓰는게 국룰.   덱은 deque import해서 append(), popleft()쓰면 됨출

# 재귀함수 (Recursive function)  자기 자신을 다시 호출 .  -재귀함수로 만들 ㅅ ㅜ있는거는 무조건 반복문으로도 만드 수 있다.
따라서 어떤게 해당 문제에서 유리할지 판단해서 선택사용stack을 사용해야할 때 구현상 스택 라이브러리 대신에 재귀함수를 이용하는경우 많음.

DFS(Depth-First Search) 깊이우선탐색 -> STACK 사용

BFS 너비우선탐색  가까운 노드부터 우선적으로 탐색
큐 자료구조를 이용

각 노드는 2차원 list로 표현한다. 단, 0번 인덱스 리스트는 비워둔다. 노드들이 1번부터 있으므로.
