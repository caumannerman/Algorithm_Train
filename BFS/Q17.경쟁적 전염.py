"""NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 바이러스 종는 1~K번까지 k가지가 있다.
시험관에 존재하는 모든 바이러스는 1초마다 상하좌우 모든 방향으로 증식하는데, 매초 번호가 낮은 종류의 바이러스부터 먼저 증식한다.
또한 증식 과정에서 특정한 칸에 이미 어떤 바이러스가 있다면, 그곳에는 다른 바이러스가 들어갈 수 없다.
시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하세요.
만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다.
이 때  X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다. 예를 들어 다음과 같이 3x3크기의 시험관에서 서로 다른 1,2,3번 바이러스가
각각 (1,1), (1,3), (3,1)에 위치해 있을 때, 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류를 계산해보겠다.

    1  2             1 1 2           1 1 2
             1초      1   2    2초    1 1 2
    3        ->       3 3      -->   3 3 2

    결과적으로 2초가 지난 뒤에 (3,2)에 존재하는 바이러스의 종류는 3번 바이러스이다. 따라서 3을 출력하면 정답이다.
"""
# 첫째 줄에 자연수 N,K가 주어지며, 각 자연수는 공백으로 구분.
# 둘 째 줄부터 N개의 줄에 시험관 정보 주어짐. 각 행은 N개의 원소로 구성, 해당 위치에 존재하는 바이러스의 번호가 주어지며, 공백으로 구분.
# 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다. 또, 모든 바이러스의 번호는 K이하의 자연수다.
# N+2번 째 줄에는 S, X, Y가 주어지며, 공백으로 구분한다. (0<=S <= 10,000, 1<= X,  Y <= N)
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 출력하라. 만약 S초 뒤에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력

# 9:15 시작

n, k = map(int, input().split())
graph = [[]]

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append([0] + temp)

s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

virus_now = []

def propagate(graph, virus, x, y):
    value = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >=1 and nx < len(graph) and ny >= 1 and ny < len(graph[1]):
            if graph[nx][ny] == 0:
                graph[nx][ny] = value
                virus.append((value, nx, ny))


def solution(graph, virus, s):

    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] != 0:
                virus.append((graph[i][j], i, j))

    virus.sort()

    for _ in range(s):
        l = len(virus)
        for k in range(l):

            propagate(graph, virus, virus[k][1], virus[k][2])
        virus = virus[k:]

solution(graph, virus_now, s)
print(graph[x][y])
print(graph)