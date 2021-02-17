"""세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오."""
# 입력 : 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다.
# 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
# 출력 : 첫째 줄에 정답을 출력한다.

import sys
input = sys.stdin.readline
a = list(input().rstrip())

tmp = ""
result = 0
# -가 나온 뒤로는 모든 숫자를 빼주도록 괄호를 칠 수 있게 된다.  따라서 -가 나오는 순간 op를 True로 바꿔주고  이후에 나오는 숫자들은 모두 빼준다.
# 그 전까지는, 즉, op가 그대로 False인 동안에는 숫자들을 모두 더해줄 수 밖에 없다.
op = False

for i in range(len(a)):
    if a[i].isdigit():
        tmp += a[i]
    else:
        if op == True:
            result -= int(tmp)
            tmp = ""
        else:
            result += int(tmp)
            tmp = ""
        if a[i] == '-':
            op = True
        else:
            continue
if op:
    result -= int(tmp)
else:
    result += int(tmp)

print(result)