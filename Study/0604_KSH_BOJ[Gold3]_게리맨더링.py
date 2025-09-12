'''

조건
- 두개의 선거구로 나누기
- 각 선거구는 한 개 이상의 구역
- 선거구 끼리는 이어져야함

구하려는 것
- 두 선거구의 인구수 차이를 최소화
- 두 선거구로 안 나눠지면 -1 출력


- 전체에서 빼는게 맞아?
- 백트래킹은 빠꾸만 하는게 아니라, 경우의 수 조합을 고려해줌
    그래서 combinations 쓰는 놈들은 다 백트래킹으로 가능
- 잔실수와, 조건을 하나둘씩 놓친다

'''
import sys
from itertools import combinations
from collections import deque

# 1. 입력 받기
n = int(sys.stdin.readline())
population = list(map(int, sys.stdin.readline().split()))

graph = [[0] for _ in range(n+1)]
areas = []

for i in range(1, n+1):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    areas.append(i)

# print(graph, areas)
#
# # 2. 조합으로 경우의 수 구하기
# cases = list(combinations(areas, 2))
# print(cases)

def area_check(casedd): # 구역끼리 연결됐는지
    case = [] # [1,2]
    for k in casedd:
        case.append(k)

    start = case[0] # 시작 구역 - 1
    case.remove(start)  # [2]
    visited = [False] * (n+1)
    visited[start] = True

    q = deque() # [1] -> [2] -> []
    q.append(start)

    while q:
        current = q.popleft() # 현재 내가 있는 구역 - 1, 2
        for i in graph[current][1:]: # [2,4] [1 3 6 5]
            if not visited[i] and i in case:
                q.append(i)
                visited[i] = True
            # if i in case:
                case.remove(i)

    if not case:
        return True
    else:
        return False

def population_count(case): # 인구수 구하는 놈
    pop_sum = sum(population) # 인구수 전체 합
    case_sum = 0 # 특정 경우의 인구 수 합
    for area in case:
        case_sum += population[area-1]

    pop_diff = abs(pop_sum - case_sum * 2) # 선거구 끼리의 인구수 차이

    return pop_diff

min_diff = sys.maxsize

# 발생한 예외 상황1 : 만일 도시가 6개면, range(1,3)여서, 3번째 도시를 안돈다.
# 발생한 예외 상황2 : A,B 구역으로 나눠졌을 때, A만 검사하는게 아니라 B도 검사해야된다.
for k in range(1,n//2): # 구역이 9개면... n//2 = 4
    cases = list(combinations(areas, k)) # k = 2 면

    # 발생한 예외 상황 : 만일 연결이 하나도 안된 도시들이 있으면 어떡할건데?
    if k == 1: # 9개중 1개 선택 1,2,3,4,5,6,
        for case in cases: # cases = [(1), (2), (3) .,,.. ]
            pop_diff = population_count(case)
            if pop_diff < min_diff:
                min_diff = pop_diff

    else: # k = 2,3,4,5......   (3,4,5,6,7,8,9,10)
        for case in cases:   # [(1,2),(1,3),(1,4),(1,5)....]
            if area_check(case):
                pop_diff = population_count(case)
                if pop_diff < min_diff:
                    min_diff = pop_diff

print(min_diff)