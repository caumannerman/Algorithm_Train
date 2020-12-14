"""DUMMY 라는 도스 게임이 있따. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자신의 몸과 부딪히면 게임이 끝난다.
게임은 N x N 정사각 보드 위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에는 벽이 있다. 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1이다.
뱀은 처음에 오른쪽을 향한다.
뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.

    1. 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
    2. 만약 이동한 칸에 사과가 있다면 , 그칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.

사과의 위치와 뱀의 이동경로가 주어질 때, 이 게임이 몇 초에 끝나는지 계산하라."""
# 첫 줄에 보드의 크기 N이 주어진다. (2~100)
# 다음 줄에 사과의 갯수 K가 주어진다.(0~100)
# 다음 K개 줄에는 사과의 위치가 주어지는데, 행, 열 순으로 입력된다. ( 사과의 위치는 모두 다르며, 맨위 맨 좌측(1,1)에는 사과가 없다.
# 다음 줄에는 뱀의 방향 변환 횟수 L이 주어진다.( 1~100 )
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며, 게임시작으로부터 X초가 끝난 뒤에 왼쪽(C가 'L')또는 오른쪽(C가 'D')으로 90도 방향을 회전시킨다는 뜻.
# X는 10,000 이하의 양의 정수이며, 방향 전환정보는 X가 증가하는 순으로 주어진다.
# 출력 - 게임이 몇초에 끝나는지 출력
from collections import deque
n = int(input())      ##############
k = int(input())     ##############
apple = []          ##############

for _ in range(k):
    a, b= map(int, input().split())
    apple.append((a,b))

loc_change = [] ##############
L = int(input())

for _ in range(L):
    x, c = input().split()
    loc_change.append((int(x),c))
loc_change.append((100,"C"))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
snake_x = 0
snake_y = 0
snakebody = deque([(0,0)])

time = 0
direc = 0

for i in range(len(loc_change)):
    if i>=1:
        timeleft = loc_change[i][0] - loc_change[i-1][0]
    else:
        timeleft = loc_change[i][0]

    while timeleft > 0:
        if snake_x + dx[direc] < 0 or snake_x + dx[direc] > n or snake_y + dy[direc] <0 or snake_y + dy[direc] > n:
            print(time+1)
            quit()
        if (snake_x + dx[direc], snake_y + dy[direc]) in snakebody:
            print(time+1)
            quit()
        time += 1
        snake_x += dx[direc]
        snake_y += dy[direc]
        snakebody.append((snake_x, snake_y))
        if (snake_x, snake_y) not in apple:
            snakebody.popleft()
        timeleft -= 1

    if loc_change[i][1] == 'D':
        direc += 1
    else:
        direc -= 1



















