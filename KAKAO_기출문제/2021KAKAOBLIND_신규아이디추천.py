import sys

input = sys.stdin.readline


def solution(new_id):
    # 가능한 문자들의 아스키코드를 저장해놓을 리스트
    # possible = [i for i in range(ord('a'), ord('z')+1)]
    # possible.extend([i for i in range(ord('A'), ord('Z')+1)])
    # possible.extend([ord("-"), ord("_"), ord(".")])
    possible = ["-", "_", "."]

    id = []
    dot_tick = False
    for i in new_id:
        if i == ".":
            if not dot_tick:
                dot_tick = True
                id.append(".")
            else:
                continue

        elif i.isdigit() or i.isalpha() or (i in possible):
            dot_tick = False
            id.append(i)

    # id가 비어있는 경우
    if len(id) == 0:
        return "aaa"
    else:
        # 양 끝 점제거
        if id[-1] == ".":
            id.pop()
            if len(id) == 0:
                return "aaa"
        if id[0] == ".":
            del id[0]
        if len(id) < 3:
            while len(id) < 3:
                id.append(id[-1])
        # 16자 이상이면 15로 짤, 맨뒤 . 이면 제거
        if len(id) > 15:
            id = id[:15] if id[14] != "." else id[:14]
        # 소문자로 변경
        answer = ''.join(id)
        return answer.lower()