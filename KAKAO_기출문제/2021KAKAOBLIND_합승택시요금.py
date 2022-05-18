"""카카오에서 만난 첫 Floyd-Warshall 알고리즘 """
# Floyd-Warshall임을 알면 금방 풀 수 있는 문제
import sys

input = sys.stdin.readline
INF = int(1e9)


def solution(n, s, a, b, fares):
    # 기본 플로이드 워셜 알고리즘대로 수행
    distance = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        distance[i][i] = 0
    for cur, next, cost in fares:
        distance[cur][next] = cost
        distance[next][cur] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if i == k:
                continue
            for j in range(1, n + 1):
                if j == i or j == k:
                    continue
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    # 여기까지가 기본 Floyd-Warshall -> 모든 노드에서 모든 노드로의 최단거리를 distance에 갱신해줌

    # 애초부터 따로 갈 때의 거리
    separate = distance[s][a] + distance[s][b]
    # i까지 같이가서 따로 감
    # 이 n개의 반복문이 모든 경우를 포함한다
    # 아예 다른 길까지 같이 가서, 각각 a, b로 향하는 경우
    # a 혹은 b까지 같이 가서 나머지 한 명만 집까지 가는 경우
    # a혹은 b를 지나쳐가고 (비효율 적인 경우) 각자 갈라져 집에 가는 경우 => a에서 각자 집에 가는 것보다 무조건 오래걸리므로 알아서 걸러진다.
    # a,b모두 지나쳐간 노드에서 각자 다시 집으로 가는 경우 ->  b혹은 a에서 내려 각자 갈라져가는 경우보다 무조건 오래걸리므로 알아서 걸러짐
    for i in range(1, n + 1):
        cost = distance[s][i] + distance[i][a] + distance[i][b]
        if cost < separate:
            separate = cost

    return separate