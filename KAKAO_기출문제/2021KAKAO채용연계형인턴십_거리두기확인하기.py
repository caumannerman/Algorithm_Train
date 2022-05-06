import sys

input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check_around_2(room, x, y):
    q = deque([(x, y, 0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[x][y] = True

    while q:
        now_x, now_y, dist = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if not visited[nx][ny] and dist < 2:
                if room[nx][ny] == "O":
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
                elif room[nx][ny] == "P":
                    return False
    del visited
    return True


def solution(places):
    result = [1] * 5
    exit_tick = False

    for place_num in range(len(places)):
        exit_tick = False
        for i in range(5):
            if exit_tick:
                break
            for j in range(5):
                if places[place_num][i][j] == "P":
                    # False가 나오면
                    if not check_around_2(places[place_num], i, j):
                        result[place_num] = 0
                        exit_tick = True
                        break
    return result