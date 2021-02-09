'''한 마을에 모험가 n명 있다. 모험가는 '공포도' 측정을 하여 공포도가 높으면 상황대처능력이 떨어진다고 평가된다.
모험가 길드를 안전하게 구성하고자 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다.
N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날  수 있는 그룹수의 최댓값을 구하는 프고그램을 작성하세요'''

# 아래의 내가 만든 중, 코드가 가장 빠른 코드

gongpo = list(map(int, input().split()))

count = 0
now = 0

for i in range(len(gongpo)):
    now += 1
    if gongpo[i] == now:
        count += 1
        now = 0

print(count)








