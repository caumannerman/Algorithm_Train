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