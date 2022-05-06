def solution(board, moves):
    height = len(board)
    width = len(board[0])

    # 너비만큼 현재 인형이 있는 가장 높은 위치를 나타내기 위해 리스트 생성
    now_height = [height] * width

    for i in range(width):
        for j in range(height):
            if board[j][i] != 0:
                now_height[i] = j
                break

    stack = []
    answer = 0
    for i in moves:
        # i-1열에 대해 인형을 뽑아내야함
        # 인형ㅇ ㅣ있다면
        if now_height[i - 1] < height:
            # 현재 인형
            now = board[now_height[i - 1]][i - 1]
            # 인형 뽑았으니 위치 이동
            now_height[i - 1] += 1

            if len(stack) == 0 or now != stack[-1]:
                stack.append(now)
            # stack도 안 비어있고 인형이 같음
            else:
                del stack[-1]
                answer += 2

    return answer