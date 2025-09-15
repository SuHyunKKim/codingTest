'''

1. 입력 받기
2. 미생물 그래프에 그리기
    - 겹치는 미생물은 죽이기
    - 완전 끊어져 있는 지 검사하기 -> 완전 끊어져있으면 그 미생물 없애기
3. 미생물 옮기기
    - 가장 큰 미생물 찾기
    - 그 미생물 부터 x 작게 -> y 작게 하기 ( x 작은게 우선이다 )
    - 어떠한 곳에도 둘 수 없는 미생물 죽이기
4. 미생물 인접한 것 찾기 -> 인접한 미생물 쌍 뽑기 -> 쌍 곱한거 더하기


- 좌표 -> 행렬 변환시
    x는 행이 가장 위쪽, y는 열이 가장 왼쪽이면 되는 것임.

-------

- 문제의 조건을 계속 빠뜨리거나, 실수함

'''


import sys
from collections import defaultdict, deque
import copy

n, q = list(map(int, sys.stdin.readline().split()))

plot_graph = [[0] * n for _ in range(n)] # 미생물 투입 용기
micro_animal = [] # 미생물들

for i in range(q):
    micro_animal.append(list(map(int, sys.stdin.readline().split()))+[i+1])

# print(micro_animal)



def bfs(x,y,visited):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    qqq = deque()
    qqq.append((x,y)) ### 실수한 부분
    micro = -1

    while qqq:
        cx, cy = qqq.popleft()
        micro = plot_graph[cx][cy]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if plot_graph[nx][ny] == micro:
                    visited[nx][ny] = 1
                    qqq.append((nx,ny)) ### 실수한 부분

    return visited, micro

def initial_plot(cord):
    r1, c1, r2, c2, micro_num = cord  # 미생물 좌표 할당, micro_num = 미생물 고유번호
    for i in range(0, r2-r1):
        for j in range(0, c2-c1):
            plot_graph[i][j] = micro_num

def plot(cord):
    r1, c1, r2, c2, micro_num = cord  # 미생물 좌표 할당, micro_num = 미생물 고유번호
    for i in range(r1, r2):
        for j in range(c1, c2):
            plot_graph[i][j] = micro_num

    visited = [[0] * n for _ in range(n)]
    micro_dict = defaultdict(int) # 미생물 종류 해시테이블

    for i in range(n): # bfs로 끊어진 미생물 찾음
        for j in range(n):
            if not visited[i][j]:
                new_visit, micro = bfs(i, j, visited)
                visited = new_visit
                micro_dict[micro] += 1

    # print(micro_dict)

    dump_list = [] # 없애버릴 미생물
    for m in micro_dict.keys(): # 끊어진 미생물 0으로 만듦
        if micro_dict[m] > 1:
            for i in range(n):
                for j in range(n):
                    if plot_graph[i][j] == m: ### 실수한 부분
                        plot_graph[i][j] = 0
            dump_list.append(m)

    for d in dump_list: # 미생물 dict에서 미생물 제거
        micro_dict.pop(d)

    # print(micro_dict)

    if 0 in micro_dict.keys():
        micro_dict.pop(0)


    micro_dict_coords = defaultdict(list) # 미생물 별 좌표 기록한 해시 테이블

    for m in micro_dict.keys(): # 미생물 갯수 세고, 미생물 좌표 저장하는 부분
        count = 0
        for i in range(n):
            for j in range(n):
                if plot_graph[i][j] == m:
                    count += 1
                    micro_dict_coords[m].append((i,j))
        micro_dict[m] = count

    ### 실수한 부분
    # sorted_micro_dict = sorted(micro_dict.items(), reverse = True) # 미생물 갯수 많은 순서로 정렬
    sorted_micro_dict = sorted(micro_dict.items(), key = lambda x: -x[1]) # 미생물 갯수 많은 순서로 정렬
    # print(sorted_micro_dict)

    # print(sorted_micro_dict)
    # print(micro_dict_coords)

    return sorted_micro_dict, micro_dict_coords



'''
2: [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
'''


def move_plot(sorted_micro_dict, micro_dict_coords):
    ### 실수한 부분 - 안에 넣어서 계속 초기화됨
    new_graph = [[0] * n for _ in range(n)]  # 미생물 투입할 새로운 용기

    for micro, micros in sorted_micro_dict:
        coords = micro_dict_coords[micro] # 미생물에 대한 좌표들
        # print(coords)
        row_sort = sorted(coords, key = lambda x: -x[0])
        # print(row_sort)
        len_row = row_sort[0][0] - row_sort[-1][0] + 1
        row_min = row_sort[-1][0]

        col_sort = sorted(coords, key = lambda x: -x[1])
        len_col = col_sort[0][1] - col_sort[-1][1] + 1
        col_min = col_sort[-1][1]

        # new_graph = [[0] * n for _ in range(n)] # 미생물 투입할 새로운 용기

        flag = 0

        for i in range(n):
            for j in range(n):
                # print(i,j)
                if new_graph[i][j] == 0:
                    ### 실수한 부분
                    # if n-1-j >= len_col and n-1-i >= len_row:
                    if n-j >= len_col and n-i >= len_row:
                        for r,c in coords:
                            new_graph[r-(row_min-i)][c-(col_min-j)] = micro
                            flag = 1
                        break
            if flag == 1:
                break

    return new_graph


def near_bfs(graph):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    qqq = deque()
    qqq.append((0,0, graph[0][0]))  ### 실수한 부분

    while qqq:
        cx, cy


# a = [(2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
#
# a.sort(key=lambda x: -x[0])
#
# print(a)


initial_plot(micro_animal[0])
a,b = plot(micro_animal[1])
new_graph = move_plot(a,b)
plot_graph = new_graph
for a in new_graph:
    print(a)

c,d = plot(micro_animal[2])
so_new_graph = move_plot(c,d)
plot_graph = so_new_graph

for a in so_new_graph:
    print(a)


e,f = plot(micro_animal[3])
very_new_graph = move_plot(e,f)

for a in very_new_graph:
    print(a)

# print(plot_graph)


