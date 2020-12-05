''' 계수 정렬 ( Count Sort ) 는 퀵,선택, 삽입 정렬과 같은 비교+위치변경의 알고리즘이 아니다.'''
# 계수 정렬 특징 : 별도의 리스트 선언.
#               데이터 크기가 제한되어 있을 때 ( 모여있어야 ) 유리
''' 데이터가 0~9의 정수들로 이루어져있다면, 크기 10의 리스트를 선언하고, 각 원소가 나올 때 마다, 새로 선언한 리스트 해당 인덱스에 1씩 추가한다 '''

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0]* ( max(array)+1 )

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')