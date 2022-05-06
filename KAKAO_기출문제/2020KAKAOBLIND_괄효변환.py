import sys

input = sys.stdin.readline

reverse_dict = {"(": ")", ")": "("}


def to_ghjh_string_and_v(s):
    if s == "":
        return ""
    idx = 0
    opener = 0
    closer = 0
    is_Olbarun = True
    # 올바른 괄호  문자열이 아님
    if s[0] == ")":
        is_Olbarun = False
    for i in range(len(s)):
        if s[i] == "(":
            opener += 1
        else:
            closer += 1
        if opener == closer:
            idx = i
            break

    # 현 시점 u = s[:idx+1] , v = s[idx+1:]
    u, v = s[:idx + 1], s[idx + 1:]
    # u가 올바른이면, u는 전체 result에 붙이고, v에 대해 이 함수 실행하면 됨
    if is_Olbarun:
        return u + to_ghjh_string_and_v(v)
    # u가 올바르지 않다면
    else:
        result = "(" + to_ghjh_string_and_v(v) + ")"
        for i in u[1:-1]:
            result += reverse_dict[i]
        return result


def solution(p):
    answer = to_ghjh_string_and_v(p)
    return answer