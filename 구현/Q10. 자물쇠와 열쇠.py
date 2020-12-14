""" 고고학자인 튜브는 고대 유적지에서 보물과  유적이 가득할 것으로 추정되는 비밀의 문을 발견했다.
문을 열려고 보니, 특이한 형태의 자물쇠로 잠겨있었고, 문앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명되어있었습니다.

    잠겨있는 자물쇠는 격자 한 칸 크기가 1x1인 NxN 크기의 정사각 격자 형태이고, 특이한 모양의 열쇠는 MxM 크기인 정사각 격자 형태로 되어있습니다.

자물쇠에는 홈이 파여 있고, 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며, 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조이다.
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며, 열쇠의 돌기와 자물쇠의 돌기가 만나서 안 된다.
 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.

 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock의 매개변수로 주어질 때, 열쇠로 자물쇠를 열 수 있으면 , true를, 열 수 없으면 false를 return 하도록 solution함수를 완성하라.
"""

# key 는 MxM 크기의 2차원 배열이다.
# lock은 NxN 크기의 2차원 배열이다.
# M은 항상 N이하다.
# key와 lock의 원소는 0 또는 1로 이루어져있다. 이때 0은 홈부분, 1은 돌기부분을 나타낸다.

m, n = map(int, input().split())
key = []
lock = []

for i in range(m):
    key.append(list(map(int, input().split())))

for i in range(n):
    lock.append(list(map(int, input().split())))


def rotate_matrix_clockwise(mat):
    n = len(mat)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-1-i] = mat[i][j]
    return result

def check(new_lock):
    lock_len = len(new_lock)//3
    for i in range(lock_len, lock_len*2):
        for j in range(lock_len, lock_len*2):
            if new_lock[i][j] != 1:
                return False

    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*n*3 for _ in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    for _ in range(4):
        key = rotate_matrix_clockwise(key)

        for i in range(1, 2*n):
            for j in range(1, 2*n):

                for k in range(m):
                    for o in range(m):
                        new_lock[i+k][j+o] += key[k][o]
                if check(new_lock):
                    return True
                else:
                    for k in range(m):
                        for o in range(m):
                            new_lock[i+k][j+o] -= key[k][o]


    return False
