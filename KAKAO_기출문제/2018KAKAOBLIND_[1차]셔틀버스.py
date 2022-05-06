import sys

input = sys.stdin.readline


# time_a time_b가 오름차순인지 bool로 리턴
def time_string_to_int(time):
    result = int(time[:2]) * 60 + int(time[3:])
    return result


def time_int_to_string(time):
    h = time // 60
    m = time % 60

    h = "0" + str(h) if h < 10 else str(h)
    m = "0" + str(m) if m < 10 else str(m)

    result = h + ":" + m
    return result


def solution(n, t, m, timetable):
    answer = 0
    timetable = [time_string_to_int(i) for i in timetable]
    timetable.sort()
    people_num = len(timetable)
    # 09:00
    now_bus_time = 540
    # m명 만큼 한 타임에 탈 수 있고, 540 ~ 540 + t * (n-1) 까지 버스 운행
    now_index_to_getin = 0
    now_empty_seat = m

    # 총 N번의 차량들에 대해
    for i in range(540, 540 + t * n, t):
        now_empty_seat = m
        while now_empty_seat > 0 and now_index_to_getin < people_num and timetable[now_index_to_getin] <= i:
            now_empty_seat -= 1
            now_index_to_getin += 1
        # 일단 앉을 수 있는 자리 넣어놓자
        if now_empty_seat > 0:
            answer = i
        else:
            # 마지막으로 앉아서 간 사람의 자리를 뺏음
            answer = timetable[now_index_to_getin - 1] - 1
    return time_int_to_string(answer)