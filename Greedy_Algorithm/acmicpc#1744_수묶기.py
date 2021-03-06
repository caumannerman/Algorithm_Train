"""길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다. 하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다. 그리고 어떤 수를 묶게 되면,
수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.
수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오."""
# 입력 : 첫째 줄에 수열의 크기 N이 주어진다. N은 10,000보다 작은 자연수이다. 둘째 줄부터 N개의 줄에, 수열의 각 수가 주어진다.
# 수열의 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
# 출력 : 수를 합이 최대가 나오게 묶었을 때 합을 출력한다. 정답은 항상 231보다 작다.


''' 틀렸던 이유 : 1이 여러개일 때 즉,  3 1 1 0이 입력이 되었을 때, 정답이 2여야함.'''
import sys
input = sys.stdin.readline
n = int(input())
p = []
m = []
result = 0
is_zero = False
for _ in range(n):
    a = int(input())
    if a > 0:
        p.append(a)
    elif a == 0:
        is_zero = True
    else:
        m.append(a)

p.sort(reverse = True)
m.sort()

for i in range(0,len(p),2):
    if i == len(p) - 1:
        result += p[i]
        break
    if p[i] == 1 or p[i+1] == 1:
        result += p[i] + p[i+1]
        continue
    result += p[i] * p[i+1]

for i in range(0,len(m), 2):
    if i == len(m) - 1:
        if not is_zero:
            result += m[i]
            break
        else:
            break
    result += m[i]*m[i+1]

print(result)