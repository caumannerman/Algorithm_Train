"""n x m크기의 금광이 있다. 금광은 1x1크기의 칸으로 나누어져있으며, 각 칸은 특정한 크기의 금이 들어있다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작한다. 맨 처음에는 첫 번째 열의
어느 행에서든 출발할 수 있다. 이후에 m번에 걸쳐 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 한다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하라

만약   1  3  3  2
      2  1  4  1
      0  6  4  7    이와 같은 금광이 있으면,
가장 왼쪽 위의 위치를 (1,1), 가장 오른쪽 아래의 위치를 (n,m)이라고 할 때, 위 예시에서는 (2,1)->(3,2)->(3,3)->(3,4)의 위치로 이동하면 총 19만큼의
금을 채굴할 수 있으며, 이때의 값이 최댓값이다."""
# 입력 : 첫 째 줄에 테스트케이스 T가 입력된다 (₩~1000)
# 매 테스트 케이스 첫 째 줄에 n과m이 공백으로 구분되어 입력된다. (둘 다 1~20)
# 둘 째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력된다. ( 1<= 각위치에 매장된 금의 개수 <= 100)
# 출력 : 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력한다. 각 테스트 케이스는 줄바꿈을 이용하여 구분한다.

t = int(input())
result = []

for _ in range(t):
    n, m = map(int ,input().split())
    a = list(map(int, input().split()))
    dp = [a[j*m: (j+1)*m] for j in range(n)]

    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]

            dp[i][j] = dp[i][j] +  max(left_down, left, left_up)
    onemax = 0
    for k in range(n):
        onemax = max(onemax, dp[k][m-1])
    result.append(onemax)

for i in result:
    print(i)