gems_dict = {}


def solution(gems):
    gem_set = set(gems)
    kind = len(gem_set)
    now_kind = 0
    for i in gem_set:
        gems_dict[i] = 0

    end = 0
    last_length = 100001
    result = [-1, -1]

    for start in range(len(gems)):
        while now_kind < kind and end < len(gems):
            # 새로운게 들어올 때만 now_kind추가
            if gems_dict[gems[end]] == 0:
                now_kind += 1
            gems_dict[gems[end]] += 1
            end += 1
        if end == len(gems):
            if now_kind < kind:
                break

        if end - start < last_length:
            last_length = end - start
            result[0], result[1] = start + 1, end

        gems_dict[gems[start]] -= 1
        if gems_dict[gems[start]] == 0:
            now_kind -= 1

    return result