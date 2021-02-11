"""알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
이 때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
   예를 들어, K1KA5CB7이라는 값이 들어오면, ABCKK13을 출력한다.
"""
# 첫 째 줄에 하나의 문자열 S가 주어진다.( 1<= S의 길이 <= 10,000)
# 출력 - 첫 째 줄에 문제에서 요구하는 값을 출력
import math
arr = list(input())
eng = []
numsum = 0

for i in arr:
    if i.isalpha():
        eng.append(i)
    else:
        numsum += int(i)

eng.sort()
if numsum != 0:
    eng.append(str(numsum))

print(''.join(eng))


"""두 번째 풀이
s = list(input())
a = 0
s.sort()
print(s)
for i in range(len(s)):
    if s[i].isalpha():
        a = i
        break
num = 0
for i in range(a):
    num += int(s[i])

result = "".join(s[a:])+str(num)
print(result)
"""
