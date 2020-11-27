a = list(input())
a.sort()
j=0
result = ""
num = 0
for i in range(len(a)):
    if ord(a[i]) > 57:
        j = i
        break

for k in range(j, len(a)):
    result += a[k]
for k in range(j):
    num += int(a[k])


print(result+str(num))



## isalpha()와 리스트.append() 그리고 리스트를 뭘 껴넣으면서 문자열로 변환하는지 결정해주는 ''.join(리스트) 이용하여 다시 풀어봐