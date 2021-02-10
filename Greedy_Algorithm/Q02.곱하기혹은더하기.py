data = input()


array = list(data)

for i in range(0, len(array)):
   array[i]=int(array[i])

    #숫자로 다 바꿔줬음


for i in range(0, len(array)-1):
    if array[i+1] == 0 or array[i+1] == 1 or array[i] == 0 or array[i] == 1:
        array[i+1]= array[i]+array[i+1]
    else:
        array[i+1]*=array[i]



print(array[len(array)-1])

### 이전의 계산을 새로 놓은 변수에 갱신하면서 ,  이전계산 + 혹은 * 다음 문자열에서 나올 숫자  이렇게 하는게 효율적인가..