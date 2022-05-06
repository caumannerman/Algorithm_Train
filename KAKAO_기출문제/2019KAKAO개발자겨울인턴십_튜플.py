import sys

input = sys.stdin.readline


def solution(s):
    # [{1,2,3}, {2,1}, {2}, {1,2,3,4}]와 같이 list가 됨
    answer = s[2:-2].split("},{")
    setlist = [set([]) for _ in range(len(answer) + 1)]


    for i in range(len(answer)):
        #각각 [2]  [2,3]과 같은 리스트 형태가 됨
        now = list(map(int,answer[i].split(",")))
        setlist[len(now)] = set(now)


    result = []
    for i in range(len(answer)):
        result.append((setlist[i + 1] - setlist[i]).pop())

    return result