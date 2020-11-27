'''한 마을에 모험가 n명 있다. 모험가는 '공포도' 측정을 하여 공포도가 높으면 상황대처능력이 떨어진다고 평가된다.
모험가 길드를 안전하게 구성하고자 공포도가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있다.
N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날  수 있는 그룹수의 최댓값을 구하는 프고그램을 작성하세요'''

N = int(input())

temp = input()
temp= temp.split()
for i in range(0,len(temp)):
    temp[i] = int(temp[i])

temp.sort()

trash = 0
count = 0


for i in range(0,len(temp)-1) :
    if temp[i] == temp[i+1]:
        continue
    else:
        if (i+1-trash)//temp[i]>=1 :
            count +=  1
            trash -= temp[i]
        else:
            continue

'''
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >=i:
        result += 1
        count = 0
        
print(result)

'''







