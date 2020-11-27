from collections import deque

# deque는 stack 과 queue의 기능을 모두 갖고있다.
# append, appendleft()
# pop, popleft()
#reverse(), remove() -> 리무브 안의 원소를 해당 덱에서 '하나'만 지움
#extend(), extendleft() 해당 리스트 혹은 덱을 이어붙임.
'''덱을 list로 바꾸려면 list() 함수 사용하면 '''
queue = deque()

queue.append(5)
queue.append(2)
queue.append(5)
queue.append(3)됨
queue.append(5)
queue.append(7)
queue.append(5)
queue.pop()
queue.appendleft(4)
queue.append(1)
queue.append(5)


while 5 in queue:
    print(queue)
    queue.remove(5)




print(queue)
