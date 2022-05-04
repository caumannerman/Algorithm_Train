import sys

input = sys.stdin.readline

def solution(id_list, report, k):
    # id별 누구를 신고했는지 set형태로 저장
    id_report_list = {}
    # 각 id별 번호를 부여 차례로..0~
    id_sequence = {}

    for i in id_list:
        id_report_list[i] = set()
    # 각 id별 번호를 부여 차례로..0~
    for i in range(len(id_list)):
        id_sequence[id_list[i]] = i

    # id_report_list에 각 id가 누구누구를 신고했는지 set(1,3,4)와 같이 저장
    for i in report:
        sender, receiver = i.split()
        id_report_list[sender].add(id_sequence[receiver])

    # 각 id 별 신고당한 횟수를 나타낼 리스트
    report_num_list = [0] * len(id_list)
    for i in id_report_list.values():
        for j in i:
            report_num_list[j] += 1

    # 처벌자 명단 0,1,5 ... 과 같이 id 순서로 저장
    punished = set()
    for i in range(len(report_num_list)):
        if report_num_list[i] >= k:
            punished.add(i)

    del report_num_list
    result = [0] * len(id_list)

    for i in id_list:
        result[id_sequence[i]] += len(id_report_list[i] & punished)

    return result