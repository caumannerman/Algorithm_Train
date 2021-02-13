# deque는 stack 과 queue의 기능을 모두 갖고있다.
# append, appendleft()
# pop, popleft()
#reverse(), remove() -> 리무브 안의 원소를 해당 덱에서 '하나'만 지움
#extend(), extendleft() 해당 리스트 혹은 덱을 이어붙임.
#덱을 list로 바꾸려면 list() 함수 사용하면 됨

""" N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결되어있는 것으로 간주한다.
이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크립의 개수를 구하는 프로그램을 작성하시오. 다음 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

      00110
      00011
      11111
      00000
  """
# 첫 번 째 줄에 얼음 틀의 세로길이 N과 가로 길이 M이 주어진다.
# 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
# 구멍이 뚫린 부분은 0, 그렇지 않은 부분은 1이다.
# 출력 - 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.


# 핵심 아이디어는 dfs함수에서는 result가 몇개인지, 신경쓰지 않는 것이다. 단지 0인 곳에서 dfs함수가 호출 되면, 연결된 모든 0들을 1로 만들어주는 것 뿐이고, 를
# 함수 밖 2중 for문 속에서 dfs를 호출 할 때마다 result에 1을 더해주는 것
n ,m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input())))

dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

count = 0
def dfs(x,y):
    data[x][y] = 1
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if newx >= 0 and newy >= 0 and newx < n and newy < m and data[newx][newy] == 0:
            dfs(newx,newy)


for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            dfs(i,j)
            count += 1

print(count)