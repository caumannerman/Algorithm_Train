"""슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다.
원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.
이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다.
역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.
실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
"""

#제한사항
"""
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

"""
n = int(input())
stages = list(map(int, input().split()))
"""
def solution(n, stages):
    ca = countsort(stages, n)

    totaluser = sum(ca)
    result = [0] * (n + 1)

    for i in range(1, n+1):
        result[i] = ca[i] / totaluser
        totaluser -= ca[i]
        if totaluser == 0:
            break

    real = []
    for i in range(1,len(result)):
        real.append((result[i], i))
    real.sort(key=lambda x: (-x[0], x[1]))

    answer = []
    for i in real:
        answer.append(i[1])

    return answer

"""


def countsort(array, n):
    carray = [0] * (n + 2)
    for i in array:
        carray[i] += 1
    return carray


def solution(n, stages):
    ca = countsort(stages, n)

    totaluser = sum(ca)
    result = []

    for i in range(1, n + 1):
########################### totaluser를 점점 작게 만들어주는데,지 totaluser가 0이 되었고, 아직 뒷쪽에 스테이지들이 더 남아있다면, 그 스테이지들의 실패율 또한 (0, 스테이지번호) 로 result에 추가해주어야함.
# 하지만 0으로 나누는 연산은 오류를 불러오니, totaluser가 0이 아닌 일반적인 경우와, totaluser가 0이 된 후, 남은 스테이지들 또한 실패율0으로 추가해주는 과정을 조건문으로 처리해줘야함 !!!!

# 위의 주석처리된 solution에서는 반복문을 한 번 더 돌지만, 초기에 result = [0]*(n+1)로 모든 스테이지들의 실패율이 0으로 되어있었으므로, totaluser가 0이 되는 순간 빠져나가도 됐지만, 여기서는 위에 쓰인 것처럼
# totaluser가 0 이 되고난 후에도 처리해줘야한다.
        if totaluser != 0:
            result.append((ca[i] / totaluser, i))
            totaluser -= ca[i]
        else:
            result.append((0, i))

    result.sort(key=lambda x: (-x[0], x[1]))

    answer = []
    for i in result:
        answer.append(i[1])

    return answer

print(solution(n, stages))