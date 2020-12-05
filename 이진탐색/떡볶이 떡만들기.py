""" 떡볶이 떡이 여러줄 있다. 길이가 일정하지 않아서, 한 봉지 안에 들어가는 떡의 총 길이를 절단기로 맞춰줘야한다.
절단기에 높이 H를 지정하면, 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 19, 14, 10,17 길이의 떡이 있고, 15로 지정하여 자른다면, 떡의 높이는 15, 14, 10, 15가 될 것이다.
손님은 잘린 4,0,0,2의 합인 6만큼의 떡을 가져간다.

    손님이 왔을 때 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라. """

# 첫 째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
# 적어도 M만큼 손님이 가져가기 위해, 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

n, m = map(int, input().split())
dduk = list(map(int, input().split()))


start = 0
end = max(dduk)
result = 0

while (start <= end):
    mid = (start + end) // 2
    total = 0

    for i in dduk:
        if i > mid:
            total += i - mid
    # 이것의 효율성은 의문.
    if total == m:
        print(mid, "정확히")
        exit()
        # 이곳이 핵심. total > m 인 곳에 result = mid 로 기록을 해두는 것은, 우리가 tatal >= m 인 total을 최적화해주는 것이 목표이기 때문.
    elif total > m:
        result = mid
        start = mid + 1
    else:
        end = mid -1

print(result, "초과공급 ")

# 이진탐색의 핵심.  조건에서 start = mid + 1 혹은 end = mid - 1을 통해, start~end 범위가 우리가 찾고자 하는 값을 벗어나게 된다면,
# start와 end는 계속 사이가 줄어, 인접하게 되고, 둘 중 target쪽에 가까운 쪽으로 합쳐지고, start와 end가 엇갈리게 되며 끝난다.
# 그렇다면, start~end가 target을 포함하지 않게 된 그 시점 직전의 mid가 우리가 찾던 값이므로, 이것을 항상 기록해두는 과정이 위 풀이의 핵심이다.