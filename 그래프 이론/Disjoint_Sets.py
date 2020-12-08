'''서로소 집합 ( Disjoint Sets )은 공통 원소가 없는 두 집합을 의미

"서로소 집합" 자료구조는 몇몇 그래프 알고리즘에서 매우 중요

  # 주요 연산 - find,  union    2가지!!
      find - 특정 원소가 속한 집합이 어떤 집합인지 알려주는 연산
      union - 합집합 연산으로, 두개의 원소가 포함된 집합을 하나로 합침'''



# 1. 부모테이블을 초기화 ( N번 노드의 부모는 초기에 N으로 설정된다 )
# 2. union연산 ( x,y노드를 union한다면, 둘의 부모 노드를 대소비교하고, 더 작은 곳을 x,y 둘 다 가리키게 한다 )
# 3. find연산은 DYnamic스럽게 간다. parent[x] 가 x가 아니라면, parent[x]를 갱신해주고, 리턴해준다. ( 지속적로 같은 set에 속한 노드들은 모두 다 최상위 노드를 가리키는 문어발 형태가 되도록 )

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x
# 개선된 방법 ( 경로 압축 )
def find_parent_Improved(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b




v,e = map(int, input().split())
parent = [0]* (v + 1)

# make itself be parent
for i in range(1, v + 1):
    parent[i] = i
# union연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end =' ')

for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

print('parentTable: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')