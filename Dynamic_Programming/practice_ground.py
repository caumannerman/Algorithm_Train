#12.5 fibo_memoization( Top-down)
'''
dp = [0]*100

def fibo(n):
    if n ==1 or n == 2:
        return 1
    else:
        if dp[n] != 0 :
            return dp[n]
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]

print(fibo(10))

'''

# 12.5 fibo_Bottom_up
'''
dp = [0]*100

dp[1], dp[2] = 1,1
n = int(input())

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
'''

# 12.5 1로 만들기 fibo_bottom_up

x = int(input())
dp = [0]*30001


def min_cal(x):
    if x == 2 or x == 3 or x==5:
        return 1
    if dp[x] != 0:
        return dp[x]
    else:
        arr = [min_cal(x-1)]
        temp = [2,3,5]
        for i in temp:
            if x%i == 0:
                arr.append(min_cal(x//i))
        dp[x] = min(arr)+1
        return dp[x]

print(min_cal(x))





