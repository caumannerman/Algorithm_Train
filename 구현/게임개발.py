'''첫 쨰 줄에 맵의 세로 크기 N 과 가로 크기 M을 공백으로 구분하여 입력. ( 3~50 사이)
    둘 째 줄에 게임 캐릭터가 있는 칸의 좌표 A,B와 바라보는 방향 d가 각각 서로 공배긍로 구분하여 주어진다.방향 d의 값으로는 다음과 같이 4가지가 존재.
    0: 북 1: 동 2: 남 3: 서
    셋 째 줄부터 N x M크기로 맵의 상태가 북쪽~남쪽 순으로 주어진다. 맵의 외곽은 항상 바다이며, 0은 육지, 1은 바다를 뜻한다.
    (캐릭터가 처음 생성된 곳은 항상 육지이다)
    ps. 왼쪽부터 체크하는데, 네 방향 모두 바다 혹은 가봤던 육지라면, 결과적으로 왔던 길로 다시 되돌아가는 것이다'''

# 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력해라
n, m = map(int, input().split())

x, y, cd = map(int, input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

direction = [3,0,1,2]

map1 = []



for _ in range(n):
    map1.append(list(map(int, input().split())))

map1[x][y] = 2
result = 1

while True:
    count = 0
    for i in range(4):

        if map1[x+dx[direction[cd]]][y+dy[direction[cd]]] == 0: #육지
             x = x+dx[direction[cd]]
             y = y+dy[direction[cd]]
             cd = direction[cd]
             map1[x][y] = 2
             result += 1
             break

        else:
            cd = direction[cd]
            count += 1

    if count == 4:
        if map1[x+dx[direction[cd-1]]][y+dy[direction[cd-1]]] != 1:
            x = x+dx[direction[cd-1]]
            y = y+dy[direction[cd-1]]
        else:
            break


print(result)




"""풀이2
n, m = map(int ,input().split())
x, y, dir = map(int, input().split())
map_data = []

dx = [ -1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    map_data.append(list(map(int,input().split())))
move_count = 0
gone = 0

while True:
    gone = 0
    for i in range(4):
        if map_data[x + dx[dir - 1 - i]][y + dy[dir - 1 - i]] == 0:
            map_data[x][y] = 2
            dir = dir - 1 - i
            if dir < 0:
                dir += 4
            x = x + dx[dir]
            y = y + dy[dir]
            move_count += 1
            print(x, y)
            gone = 1
            break
        else:
            dir -= 1
            if dir == -1:
                dir = 3

    if gone == 0:
        if map_data[x - dx[dir]][y - dy[dir]] != 1:
            map_data[x][y] = 2
            x = x - dx[dir]
            y = y - dy[dir]
            move_count += 1
            print(x, y)
        else:
            print(move_count)
            exit()


"""

