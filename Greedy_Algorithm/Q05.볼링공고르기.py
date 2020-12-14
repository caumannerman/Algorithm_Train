""" A, B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다. 볼링공은 총 N개가 있으며, 각 볼링공마다 무게가 적혀있고, 공의 번호는 1번부터 순서대로 부여됩니다.
또한 같은 무게의 공이 여러개 있을 수 있지만, 서로 다른 공으로 간주한다. 볼링공의 무게는 1부터 M까지 자연수 형태로 존재한다.

예를 들어 N이 5이고, M이 3이며 각각의 무게가 차례대로 1, 3, 2, 3, 2일 때 각 공의 번호가 차례대로 1번부터 5번까지 부여된다. 이 떄 두 사람이 고를 수 있는 볼링공 번호의 조합을 구하면 다음과 같다.

    (1,2),  (1,3), (1,4), (1,5), (2,3), (2,5), (3,4), (4,5)

     결과적으로 두 사람이 공을 고르는 경우의 수는 8가지이다. N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하라.  """

# 첫 째 줄에 볼링공의 수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어진다. ( N은 1~1000, M은 1~10 )
# 둘 째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어진다. ( 1<= K <= M )

# 출력 - 첫 째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력한다.


# 풀이 1/2 - itertools의 combinations 함수 사
'''
from itertools import combinations

n, m = map(int, input().split())
weight = list(map(int, input().split()))

combi = list( combinations(weight,2))

result = len(combi)
for i in combi:
    if i[0] == i[1]:
        result -= 1

print(result)

'''

# 풀이 2/2용 - counting sort 응용
n, m = map(int, input().split())
data = list(map(int, input().split()))

arr = [0]*(m + 1)

for i in data:
    arr[i] += 1

result = 0
for i in arr[1:]:

    result += i * (n - i)
    n -= i

print(result)