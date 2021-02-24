"""N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오."""
# 입력 : 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
# 출력 : 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

n = int(input())
result = [0] * n
visited = [False] * n
count = 0


def possi(level, cdd):
    for i in range(level):
        if visited[cdd] or level - i == abs(result[i] - cdd):
            return False
    return True


def dfs(level):
    if level == len(result):
        global count
        count += 1
        return
    for i in range(n):
        if possi(level, i):
            result[level] = i
            visited[i] = True
            dfs(level + 1)
            visited[i] = False


dfs(0)
print(count)