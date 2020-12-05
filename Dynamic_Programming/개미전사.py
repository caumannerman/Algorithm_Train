""" 개미전사는 부족한 식량을 충당하고자 메뚜기마을 식량창고를 몰래 공격하려고 한다. 메뚜기마을 에는 여러 식량창고가 있는데, 이들은 일직선으로 이어져있다.
각 식량창고에는 정해신 식량이 있으며, 개미전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다.
이 때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다. 따라서 개미전사가 들키지 않고 약탈하기 위해서는
최소 한 칸 이상 떨어진 식량 창고를 털어야한다. 예를 들어 식량창고 4개가 당므과 같이 존재한다고 한다.

[1, 3, 1, 5]  -> 2,4번째 창고를 털면 최대 식량 얻을 수 있다.

이렇게 일직선 상의 식량창고에서 최대한 많은 식량을 얻기를 원할 때, 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때, 얻을 수 있는 최댓값을 구하는 프로그램 작성하라 """

# 첫 쨰  줄에 식량창고 개수 N이 주어진다 .( 3<= N <= 100 )
# 둘 째 줄에 공백으로 구분되어 각 식량창고에 저장된 식량의 개수 K가 주어진다.(0 <= K <= 1000 )
# 첫 째 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.
import time

n = int(input())

arr = list(map(int, input().split()))

# Top-Down Dynamic-Programming -- little bit slower than bottom-up
'''
dp = [0]*(n+1)
def thief(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)
    if dp[len(arr)] == 0:
        dp[len(arr)] = max(arr[-1] + thief(arr[:-2]), thief(arr[:-1]))
    return dp[len(arr)]
    
start = time.time()

print(thief(arr))

end = time.time()

print(end - start)

'''

# Bottom-Up Dynamic Programing  --- 이게 더 빠르다!!!!!!


d = [0]*n

start = time.time()

d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2,n):
    d[i] = max(arr[i] + d[i-2] , d[i-1])

print(d[n-1])
end = time.time()
print(end-start)
