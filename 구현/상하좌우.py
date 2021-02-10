"""여행가 A는 NxN크기의 정사각형 공간위에 이다. 1,1 위치에서 출발하여 상,하,좌,우 로 이동할 수 있다.
첫 째 줄에 공간의 한 변의 길이 N이 주어지고, 두번째 줄에 이동계획이 L L R U D와 같이 공백을 기준으로, L,R,U,D로 주어진다.
1,1에서 왼쪽 혹은 위로 움직이는 것과 같은 불가능한 움직임은 무시된다. 이동계획을 모두 마치고난 후 위치를 공백을 기준으로 출력해라."""
n = int(input())
data = list(input().split())
# 굳이 1,1 리스트로 안 놓고, 그냥 x,y로 별개의 변수로 두는 것이 더 효율적일 수도 있다.
x, y = 1, 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

D = ['R', 'L', 'D', 'U']

for i in data:
    for j in range(len(D)):
        if i == D[j]:
            if x + dx[j] > 0 and y + dy[j] > 0 and x + dx[j] <= n and y + dy[j] <= n:
                x += dx[j]
                y += dy[j]
                break

print( y,x)












