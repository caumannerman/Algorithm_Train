""" 데이터 처리 전문가가 되고 싶은 '어피치'는 문자열을 압축하는 방법에 대해 공부하고 있다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고있는데, 문자열에서 같은 값이 연속해서 나타나는 것을
그 문자의 개수와 반복되는 값으로 표현하여 , 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있다.
간단한 예로 "aabbaccc"의 경우, '2a2ba3c' ( 문자 반복 없이 한 번 나오는 경우는 1을 써주지 않음 )와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있다.
예를 들면, 'abcabcdede'와 같은 문자열은 압축되지 않는다. 이 단점을 해결하기 위해 문자열을 1개 이상 단위로 잘라 압축하는 방법 찾으려 한다.

예를 들어, 'ababcdcdababcdcd'의 경우 문자를 1개단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라 압축하면, '2ab2cd2ab2cd'로 표현 가능하다. 다른 방법으로 8개 단위로 잘라 압축한다면 '2ababcdcd'로 표현할 수 있고,
이때가 가장 짧게 압축하여 표현할 수 있는 방법이다.
다른 예로 'abcabcdede'는 2개 단위로 압축하면 'abcabc2de'가 되고, 3개 단위로 자르면, '2abcdede'가 되어 이것이 가장 짧은 방법이 된다.
이 때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여준다.
압축할 문자열 s가 주어질 때, 위의 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution함수를 완성해라."""
# s 의 길이는 1이상 1000이하
# s는 알파벳 소문자로만 이루어져있다.


s = list(input())

def solutions(s):
    min_arr = []
    for i in range(1, len(s)//2+1):
        arr = []
        iter = i
        temp = ""
        for j in range(len(s)):

            temp += s[j]
            iter -= 1
            if iter == 0:
                arr.append(temp)
                iter = i
                temp = ""
        arr.append(temp)

        min_len = len(s)
        succesive = 0
        for k in range(1, len(arr)):

            if arr[k] == arr[k-1]:
                succesive += 1
            else:
                if succesive == 0:
                    pass
                elif succesive == 1:
                    min_len -= i-1
                else:
                    min_len -= succesive*i-1
                succesive = 0
        min_arr.append(min_len)
    return min(min_arr)


print(solutions(s))



