""" 가로 길이가 N, 세로 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 이 얇은 바닥을  1X2 의 덮개,  2X1의 덮개, 2X2 의 덮개를 이용해 채우려한다.
이 떄 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오. ( 예를 들어 2X3크기의 바닥을 채우는 경우의 수는 5가지이다 ) """

# 첫 줄에 N이 주어진다. ( 1<= N <= 1000 )
# 2xN 크기의 바닥을 채우는 방법 수를 796796으로 나눈 나머지를 출력하라.

n = int(input())

dp = [0]*1001

# Dynamic Bottom- up
'''
dp[1] = 1
dp[2] = 3


for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % 796796
# 애초에 dp Table에 저장할 때, 796796으로 나눈 나머지를 저장해도 된다!

print(dp[n]%796796)

'''

# Dynamic Top-Down

def tile(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if dp[n] != 0:
        return dp[n]
    dp[n] = ( tile(n-1) +tile(n-2) *2)%796796
    return dp[n]

print(tile(n))


