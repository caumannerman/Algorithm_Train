'''N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과 성적이 주어졌을 때, 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하'''

# 첫 째 줄에 학생 수 N이 입력됨
# 2 ~ N + 1 째 줄까지 학생이름 성적  형태로 ' ' 으로 구분되어 입력된다.( 성적은 100이하 자연수)
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.

n = int(input())
arr = []

for _ in range(n):
    a, b = input().split()
    arr.append((int(b), a))

arr.sort()

for i in arr:
    print(i[1], end = ' ')

"""  조금 더 세련된 방법  

for _ in range(n):
    a, b = input.split()
    arr.append(a, int(b))

arr = sorted(arr, key = lambda x:x[1])

"""