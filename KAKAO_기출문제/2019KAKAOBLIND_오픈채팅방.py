import sys

input = sys.stdin.readline

uidDict = {}


def solution(record):
    # 여기에는 Enter, Leave인 경우의 uid만 담아서, dict에 담긴 uid: nickname쌍으로 뿌려줄 때 사용
    # 0 - Enter , 1 - Leave, 2 - Change
    temp = []
    answer = []

    for i in record:
        if i[0] == "L":
            temp.append((1, i.split(" ")[1]))
            continue
        kind, b, c = i.split(" ")
        if kind == "Enter":
            temp.append((0, b))
        uidDict[b] = c

    for kind, uid in temp:
        # Enter
        if kind == 0:
            answer.append(uidDict[uid] + "님이 들어왔습니다.")
        # Leave
        else:
            answer.append(uidDict[uid] + "님이 나갔습니다.")

    return answer