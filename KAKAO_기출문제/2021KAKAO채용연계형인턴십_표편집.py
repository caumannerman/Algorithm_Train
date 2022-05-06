import sys

input = sys.stdin.readline

nodes = {}


def solution(n, k, cmds):
    for i in range(1, n - 1):
        nodes[i] = [i - 1, i + 1]
    nodes[0] = [n - 1, 1]
    # 끝 노드
    nodes[n - 1] = [n - 2, 0]

    # 삭제 노드 저장해둘 stack
    deleted = []

    for cmd in cmds:
        # 이동 U or D
        if len(cmd) > 1:
            dir, move_num = cmd.split(" ")
            move_num = int(move_num)
            if dir == "D":
                while move_num > 0:
                    k = nodes[k][1]
                    move_num -= 1
            # U _ 일 때
            else:
                while move_num > 0:
                    k = nodes[k][0]
                    move_num -= 1
        # C혹은 Z
        else:
            if cmd == "C":
                # 앞 노드의 뒷 value
                nodes[nodes[k][0]][1] = nodes[k][1]
                # 뒷 노드의 앞 value
                nodes[nodes[k][1]][0] = nodes[k][0]
                deleted.append((k, nodes[k][0], nodes[k][1]))

                # k를 변경하기 전에 삭제
                del nodes[k]
                # 삭제 후 새로운 곳 선택 (바로 밑) -> 끝이면 바로 위
                # 맨 밑을 삭제한 경우
                if deleted[-1][2] == 0:
                    k = deleted[-1][1]
                else:
                    k = deleted[-1][2]


            # Z(삭제 복구)
            else:
                idx, former, next = deleted.pop()
                nodes[former][1] = idx
                nodes[next][0] = idx
                nodes[idx] = [former, next]
    result = ""
    for i in range(n):
        if nodes.get(i) != None:
            result += "O"
        else:
            result += "X"
    return result







