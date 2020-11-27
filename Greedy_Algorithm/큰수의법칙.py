'''다양한수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 만들 수 있는 가장 큰 수를 구하는 문제.
      같은 수는 최대 K번 연속하여 더할 수 있고, 배열의 서로 다른 인덱스에 해당하는 수가 같은 경우에는 서로 다른 숫자로 간주한다.

      첫 째 줄에 배열의 크기, M, K 값을 ' '으로 구분하여 입력받고, 두 번 째 줄에서 배열을 ' '으로 구분하여 입력받는다'''

n, m, k = map(int, input().split())

data = list(map(int, input().split()))


data.sort()

result = 0

if data[-1] == data[-2]:
    result = data[-1]*m

else:
    result = ( k*data[-1] + data[-2] ) * (m//(k+1)) +( m%(k+1))*data[-1]


print(result)