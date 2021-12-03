"""평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어졌고, 고민 끝에 카카오 TV라이브 방송을 하기로 마음먹었다.
그냥 먹방을 하면 다른 방송과 차별이 없기에 다음과 같은 독특함을 생각해냈다.

회전판에 먹어야 할 N개의 음식이 있다. 각 음식에는 1부터 N까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다. 무지는 다음 방법으로 음식을 먹는다.

    1. 무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
    2. 마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
    3. 무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다. 다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식이다.
    4. 회전판이 다음 음식을 무지 앞으로 가져오는 데 걸리는 시간은 없다고 가정한다.


무지가 먹방을 시작힌 지 K초 후에 네트워크 장애로 방송이 중단됐다. 무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 먹어야하는지 알고자합니다.
각 음식을 모두 먹는 데 필요한 시간이 담겨있는 배열 food_times, 네트워크 장애가 발생한 시간 K초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return하도록 solution함수를 완성하세요."""

# food_times 는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어있는 배열입니다.
# k는 방송이 중단된 시간을 나타낸다.
# 만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 된다.

import heapq


food_times = list(map(int, input().split()))
k = int(input())
'''
def solution(food_times, k):
    leng = len(food_times)
    while True:
        for i in range(leng):
            if food_times[i] != 0:
                food_times[i] -= 1
                k -= 1
            if k == 0:
                return i+2

'''


def solution(food_times, k):
    jmin = 0
    rest_len = len(food_times)

    while True:
        if k < rest_len:
            k += 1
            for i in range(len(food_times)):
                if food_times[i] >= jmin + 1:
                    k -= 1
                    if k == 0:
                        return i + 1

        else:
            jmin += 1
            k -= rest_len
            rest_len -= food_times.count(jmin)
            if rest_len == 0:
                return -1

    return answer


# 위의 코드는 정확성  테스트는 모두 통과하나, 효율성에서 모두 실패..

# 우선순위 큐를 이용하여 처리해 주는 것이 Point

import heapq





def solution(food_times, k):
    q = []
    for i in range(len(food_times)):
        heapq.heappop(q, (food_times[i], i + 1))

    rest_food = len(food_times)
    former_del = 0

    while q:

        if k >= (q[0][0] - former_del) * rest_food:
            now_time, _ = heapq.heappop(q)
            k -= (now_time - former_del) * rest_food
            rest_food -= 1
            former_del = now_time
        else:
            q.sort(key=lambda x: x[1])
            idx = k % rest_food
            return q[idx][1]
    return -1
