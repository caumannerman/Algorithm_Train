""" 떡볶이 떡이 여러줄 있다. 길이가 일정하지 않아서, 한 봉지 안에 들어가는 떡의 총 길이를 절단기로 맞춰줘야한다.
절단기에 높이 H를 지정하면, 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
예를 들어 19, 14, 10,17 길이의 떡이 있고, 15로 지정하여 자른다면, 떡의 높이는 15, 14, 10, 15가 될 것이다.
손님은 잘린 4,0,0,2의 합인 6만큼의 떡을 가져간다.

    손님이 왔을 때 요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하라. """

# 첫 째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다.
# 적어도 M만큼 손님이 가져가기 위해, 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
n , m = map(int, input().split())
data = list(map(int, input().split()))


def cut(n):
    result = 0
    for i in data:
        if n < i:
            result += (i - n)
    return result

def binsch(target):
    start = 0
    end = max(data)
    last = 0
    while True:
        mid = (start + end) // 2

        if cut(mid) == target:
            return mid
        elif cut(mid) < target:
            end = mid - 1
        else:
            last = mid
            start = mid + 1

        if start > end:
            break
    return last


print(binsch(m))
