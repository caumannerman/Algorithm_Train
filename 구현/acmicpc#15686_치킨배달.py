""" 도저히 알고리즘이 생각이 나지 않으면, 모든 경우를 탐색하는 경우를 생각해라!!!!
itertools의 combinations, permutations, product등 , 그리고 백트래킹..... """

import sys
input = sys.stdin.readline
from itertools import combinations
n ,m = map(int, input().split())
dosi = []


for _ in range(n):
    dosi.append(list(map(int, input().split())))

chicken = [(i,j) for i in range(n) for j in range(n) if dosi[i][j] == 2]
house = [(i,j) for i in range(n) for j in range(n) if dosi[i][j] == 1]

def dosiminimum(house, sortedchicken):
    result = 0
    for i in house:
        housemin = int(1e9)
        for j in sortedchicken:
            housemin = min(housemin, abs(i[0] - j[0]) + abs(i[1] - i[1]))
        result += housemin
    return result

finalresult = int(1e9)
if len(chicken) == m:
    print(dosiminimum(house, chicken))
else:
    for i in combinations(chicken, m):
        finalresult = min(finalresult, dosiminimum(house, i))
    print(finalresult)