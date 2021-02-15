"""세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다.
이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

배열 A와 B의 인덱스는 1부터 시작한다."""
# 입력 : 첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다.
# 둘째 줄에 k가 주어진다. k는 min(109, N2)보다 작거나 같은 자연수이다.
# 출력 : B[k]를 출력한다.

import sys

input = sys.stdin.readline
n = int(input().rstrip())
k = int(input().rstrip())

#우리는 k번째로 큰 수가 뭔지 구하고싶다. 즉 k번째 오는 숫자의 값을 알고싶다.
# 거꾸로 생각해서, 우리는 x라는 숫자가 일차원배열 b에서 몇번째 위치에 오는지를 알 수 있다.
#이는 2차원 배열 a에서 각 행의 번호(1번~n)로 x를 나누면 그 행에 있는 x보다 작거나 같은 숫자의 갯수를 구할 수 있다. 물론 x//행번호 가
# 2차원 배열의 열 갯수인 n보다 크면, 그 행에 존재하는 모든 수가 x보다 작다는 말이니까 min( x//행번호, 그 행의길이(즉 열 갯수 = n))처
def small_or_equal(s):
    result = 0
    for i in range(1, n + 1):
        result += min(s // i, n)리
    return result


def bs(target, start, end):
    last_r = 0
    while True:
        mid = (start + end) // 2
        if small_or_equal(mid) < target:
            start = mid + 1
# 이곳이 가장 어려운 부분. ==> small(mid)가 mid숫자보자 작은것이 몇개 있는지 알려주는데, 이 mid숫자가 배열에 없는 숫자(예를 들면 소수)
#다 일 수도 있다. 그런 경우에는 예를들어 구하고자하는 77번째 값이 100인데, 101이라는 소수에 대한 small(101)값 == target이 된다.
#따라서 small(mid) == target이라고 해서 바로 mid를 return해주면 틀린다!!!
# 어쨌든 이분탐색은 1 ~ n*n까지 모든 수를  다 check할 수 있는것이니까 일단 small(mid) >=target이면 저장해놓고 넘겨야한다.
#반복문이 끝날때까지. 그래야 올바른 값을 구할 수 있다.
        else:
            last_r = mid
            end = mid - 1
        if start > end:
            break
    return last_r


print(bs(k, 1, n * n))