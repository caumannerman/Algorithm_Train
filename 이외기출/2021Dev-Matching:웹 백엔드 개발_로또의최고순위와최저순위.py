place = {0: 7, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}


def solution(lottos, win_nums):
    answer = []
    zero_num = lottos.count(0)
    count = 0
    for i in lottos:
        if i in win_nums:
            count += 1
    answer.append(place[count + zero_num] if place[count + zero_num] != 7 else 6)
    answer.append(place[count] if place[count] != 7 else 6)

    return answer