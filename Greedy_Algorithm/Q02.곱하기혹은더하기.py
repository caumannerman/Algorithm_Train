"""각 자리가 숫자 (0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 X 혹은 +연산자를 넣어
결과적으로 만들어질 수 있는 가장 큰수를 구하는 프로그램을 작성하세요.
단, +보다 *를 먼저 계산하는 일반적 방식이 ㅏ니라, 연산은 모두 왼쪽부터 순서대로 진행한다.
"""
#입력 - 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어진다
#첫 째 줄에, 만들어질 수 있는 가장 큰 수를 출력


s = list(map(int, input()))
result = s[0]

mid = 0

for i in range(1,len(s)):
    if result <= 1:
        result += s[i]
        continue
    mid = i
    break

for i in range(mid, len(s)):
    if s[i] == 0 or s[i] == 1:
        result += s[i]
    else:
        result *= s[i]

print(result)