import sys
from itertools import combinations
from bisect import bisect_left
input = sys.stdin.readline

dic = {}

#이진탐색을 구현했었으나, from bisect import bisect_left로 대체

def solution(info, query):
    for i in info:
        now = i.split()
        # 점수만 제외하고 리스트로 갖고옴 -> 길이는 무조건 4
        now_key = now[:-1]
        # 점수만 -> value
        now_val = int(now[-1])
        del now

        #여기가 0이어야하는 것이 중요!!!! ""도 key에 포함 되어야한다.  다른 조건 없이 점수로만 실행하는 쿼리도 있으므로...
        for j in range(0, 5):
            possi_keys = combinations(now_key, j)

            for k in possi_keys:
                combikey = ''.join(k)
                if dic.get(combikey):
                    dic[combikey].append(now_val)
                else:
                    dic[combikey] = [now_val]
    # 이분탐색을 위해 정렬
    for i in dic.values():
        i.sort()


    answer = []
    for i in query:
        i = i.replace("and", "").split()
        now_key = ''.join(i[:-1]).replace("-","")
        now_score = int(i[-1])
        if dic.get(now_key):
            idx = bisect_left(dic[now_key], now_score)
            answer.append(len(dic[now_key]) - idx)
        else:
            #무수한 런터임오류 test case를 만들어낸 주범이 이것. 쿼리 조건에 없는 key면 0명으로 결과에 붙여줌
            answer.append(0)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query =["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))
