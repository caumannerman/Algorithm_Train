import sys

input = sys.stdin.readline
import heapq


# 문자열 형태의 시간을 초단위로 바꾸어 int형으로 return
def strTosec(time):
    h = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:])
    return h + m + s


# 초단위 int형 시간을 문자열 "hh:mm:ss"로 바꾸어 return
def secTostr(time):
    h = str(time // 3600)
    temp = time % 3600
    m = str(temp // 60)
    s = str(temp % 60)
    return h.zfill(2) + ":" + m.zfill(2) + ":" + s.zfill(2)


def solution(play_time, adv_time, logs):
    play_time = strTosec(play_time)
    ad_time = strTosec(adv_time)

    # log의 시작시간과 끝시간을 모두 차례로 뽑아서
    # 각 초마다 몇 명이 재생을 하고있는지 새로운 배열에 저장할 것이다.
    # 마지막인덱스 ( dp[play_time]은 의미없다. 무시하면 됨)
    dp = [0] * (play_time + 1)
    for r in logs:
        log_start = strTosec(r[:8])
        log_end = strTosec(r[9:])
        # 시작시점은 1로 표시
        dp[log_start] += 1
        # 시청 종료시점은 -1로 표시
        dp[log_end] -= 1
    # 0000 1 00 -1 00 2 1 -1 00 과 같은 형태가 된다.


    # dp가 각 시점에 몇 명이 시청하고있는지를 나타내게 됨
    for i in range(1, play_time + 1):
        dp[i] += dp[i-1]
    # dp가 각 시점까지 몇명 시청을 했는지 "누적"시청자를 나타내게 됨
    for i in range(1, play_time + 1):
        dp[i] += dp[i-1]


    max_count = dp[ad_time - 1]
    max_start_time = 0
    for i in range(ad_time, play_time):
        now_count = dp[i] - dp[i - ad_time]
        if now_count > max_count:
            max_count = now_count
            max_start_time = i - ad_time + 1

    # 00001111122222233333222211122222333444444432111111001122 이런 배열을 만들것

    answer = secTostr(max_start_time)
    return answer