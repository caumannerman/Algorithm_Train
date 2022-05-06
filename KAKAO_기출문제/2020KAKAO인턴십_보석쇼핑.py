gems_dict = {}


def solution(gems):
    gem_set = set(gems)
    for i in gem_set:
        gems_dict[i] = 0

    end = 0
    last_length = 100001
    result = [-1, -1]
    for start in range(len(gems)):
        while 0 in gems_dict.values() and end < len(gems):
            gems_dict[gems[end]] += 1
            end += 1
        if end == len(gems):
            if 0 in gems_dict.values():
                break

        if end - start < last_length:
            last_length = end - start
            result[0], result[1] = start + 1, end
        gems_dict[gems[start]] -= 1

    return result