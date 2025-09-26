'''


문제 쪼개기


- 입력 받기

- 아침시간
    신앙심 1 얻기



- 점심 시간
    그룹 형성 - 신봉 음식 동일할 때
    그룹 대표자 선정 - 신앙심 큰사람 -> x 가장 작은 사람, y 가장 작은 사람
    대표자에게 신앙심 넘기기

    BFS로

- 저녁 시간

놓친 부분
- 내가 자꾸 업데이트 된 그 boss 정보를 안 사용 함. 과정에서 boss도 업데이트 됨을 잊음
- 방어 상태를 잘 못 처리함. 당일만 고려하는게 아니라, 그 다음날이 됐을 때, 방어상태가 해제됨.
-> 당일에만 focus 하면 안되고, 당일에 일어나는 변화 + 다음날이 될 때 일어나는 변화 둘 다를 잘 알아야함.


'''

from collections import deque, defaultdict

def bfs(food_graph, b_graph, visited, x,y):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    group = []

    q = deque() # 데크
    visited[x][y] = True ### 이거 또 빼먹음
    q.append((x,y,food_graph[x][y]))

    group.append([x,y, b_graph[x][y], food_graph[x][y]] ) # 초기 그룹 생성, ### 나중에 튜플 인덱싱 안되니까 리스트로 넣자

    while q:
        cx, cy, c_food = q.popleft()
        # print(c_food)
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and food_graph[nx][ny] == c_food:
                # print("NONO")
                # print(food_graph[nx][ny], c_food)
                group.append([nx, ny, b_graph[nx][ny], food_graph[x][y]]) # 그룹에 학생 추가

                visited[nx][ny] = True
                q.append((nx, ny, food_graph[nx][ny], ))


    return group, visited


def morning(b_graph):

    for i in range(n):
        for j in range(n):
            b_graph[i][j] = b_graph[i][j] + 1

    return b_graph

def lunch(food_graph, b_graph):

    visited = [[0] * n for _ in range(n)] # 방문 여부 리스트

    groups = [] # 생성된 그룹들을 모아둔 녀석

    ''' 그룹 만들기 '''
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group, new_visited = bfs(food_graph, b_graph, visited, i, j)

                visited = new_visited # visited 업데이트

                groups.append(group)

    ''' 신앙심 대표한테 넘기기 '''
    boss_list = [] # 대표자 목록

    sorted_groups = [] # 대표자를 필두로 정렬된 그룹

    for group in groups:
        if len(group) == 1: # 그룹이 한명이면 넘어가기
            boss_list.append(group[0]) ### 이 부분 부분 디버깅으로 잡아냈음. 매우 다행
            sorted_groups.append(group)
            continue
        else:
            sorted_group = sorted(group, key=lambda x: (-x[2], x[0], x[1])) # 그룹 정렬
            sorted_groups.append(sorted_group)
            boss = sorted_group[0] # 대표자
            # print(boss)
            for student in sorted_group[1:]: # boss 제외 일반 학생들의 신앙심 대표한테 주기
                boss[2] += 1
                b_graph[boss[0]][boss[1]] += 1 ### 신앙심 그래프에도 반영을 해줘야지.
                b_graph[student[0]][student[1]] -= 1

            boss_list.append(boss)

    return sorted_groups, boss_list, b_graph


def dinner(boss_list, food_graph, b_graph):

    ''' 전파 순서 정하기 '''

    '''
    spread_dict = defaultdict(list) # 음식에 따라 대표자를 넣은 해시

    for boss in boss_list:
        boss = boss + [0] # 전파 여부를 넣는중
        spread_dict[boss[3]] += [boss] ### 이거 반드시 묶어야 된다

    sorted_spread_dict = defaultdict(list)

    for key in spread_dict.keys():
        # sorted_list = sorted(spread_dict[key], key=lambda x: (-x[2], x[0], x[1]))
        sorted_list = sorted(spread_dict[key], key=lambda x: (len(x[3]), -x[2], x[0], x[1]))
        sorted_spread_dict[key] = sorted_list
    '''

    sorted_boss_list = sorted(boss_list, key=lambda x: (len(x[3]), -x[2], x[0], x[1]))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    flag_graph = [[0] * n for _ in range(n)]

    ''' 전파 하기 '''
    # order = ["T", "C", "M", "CM", "TM", "TC", "TCM"] # 음식 전파 순서
    # for o in order:
    '''
    for boss in sorted_spread_dict.values():
        print(boss)
    '''

    for boss in sorted_boss_list:
        # if not boss[4]: # 만일 전파가 안됐다면
        if not flag_graph[boss[0]][boss[1]]: # 만일 전파가 안됐다면
            # please_score = boss[2] - 1 # 간절함 수치
            please_score = b_graph[boss[0]][boss[1]] - 1 # 간절함 수치
            # direction = boss[2] % 4 # 방향
            direction = b_graph[boss[0]][boss[1]] % 4 # 방향


            b_graph[boss[0]][boss[1]] = 1 ### 이 조건 빼먹음
            # boss_food = boss[3] # 대표자의 음식
            boss_food = food_graph[boss[0]][boss[1]] # 대표자의 음식

            cx = boss[0]
            cy = boss[1]

            while please_score > 0:
                cx += dx[direction]
                cy += dy[direction]
                nx = cx
                ny = cy

                # nx = cx + dx[direction]
                # ny = cy + dy[direction]
                if 0<=nx<n and 0<=ny<n: # 겪자 밖이 아니라면
                    if food_graph[nx][ny] == boss_food: # 만일 대표자와 전파대상 음식이 같으면
                        continue
                    else:                               # 음식이 다르면
                        if please_score > b_graph[nx][ny]: # 강한 전파
                            food_graph[nx][ny] = boss_food
                            please_score = please_score - (b_graph[nx][ny]+1)
                            b_graph[nx][ny] += 1
                            flag_graph[nx][ny] = 1
                        else:                              # 약한 전파
                            b_graph[nx][ny] += please_score
                            please_score = 0               # 이거 순서 중요

                            food = food_graph[nx][ny] + boss_food
                            food = set(food)
                            # print(food, len(food))

                            if len(food) == 3:
                                food_graph[nx][ny] = "TCM"
                            elif len(food) == 2:
                                if "T" not in food:
                                    food_graph[nx][ny] = "CM"
                                elif "C" not in food:
                                    food_graph[nx][ny] = "TM"
                                elif "M" not in food:
                                    food_graph[nx][ny] = "TC"
                            else:
                                food_graph[nx][ny] = list(food)[0]

                            flag_graph[nx][ny] = 1
                            # print(food_graph[nx][ny])
                else:
                    break

        # else:
        #     boss[4] = 0

        #
        # for l in b_graph:
        #     print(l)
        # for l in food_graph:
        #     print(l)

    return sorted_boss_list, food_graph, b_graph

def cal_food_score(food_graph, b_graph):

    scores = defaultdict(int)
    order = ["TCM", "TC", "TM", "CM", "M", "C", "T"]
    for o in order:
        scores[o] = 0
        for i in range(n):
            for j in range(n):
                if food_graph[i][j] == o:
                    scores[o] += b_graph[i][j]
    return scores

# b_graph = morning(b_graph)
#
# for l in b_graph:
#     print(l)
#
# groups, boss_list, b_graph = lunch(food_graph, b_graph)
#
# print(boss_list)
#
# for l in b_graph:
#     print(l)
#
# sorted_spread_dict, food_graph, b_graph = dinner(boss_list, food_graph, b_graph)
#
# for l in b_graph:
#     print(l)
#
# scores = cal_food_score(food_graph, b_graph)
#
# print(scores)

# print(b_graph) # 점심시간 신앙심 업데이트 된 것
# print(groups) # 그룹 목록
# print(boss_list) # 대표자 목록
# print(sorted_spread_dict)

if __name__ == "__main__":
    for _ in range(1,2):
        n, t = list(map(int, input().split()))  # 행렬 크기 n, 날수 t

        food_graph = []  # 초기 음식 그래프
        for _ in range(n):
            food_graph.append(list(input()))

        b_graph = []  # 초기 신앙심 그래프
        for _ in range(n):
            b_graph.append(list(map(int, input().split())))

        for _ in range(t):
            b_graph = morning(b_graph)
            # print(b_graph)

            # for l in b_graph:
            #     print(l)

            groups, boss_list, b_graph = lunch(food_graph, b_graph)
            # print(boss_list, b_graph)
            # print(f'boss_list: {boss_list}')
            # for l in food_graph:
            #     print(l)
            # for l in b_graph:
            #     print(l)

            sorted_boss_list, food_graph, b_graph = dinner(boss_list, food_graph, b_graph)
            # print(food_graph, b_graph)
            # for l in food_graph:
            #     print(l)
            # for l in b_graph:
            #     print(l)
            scores = cal_food_score(food_graph, b_graph)

            # print(b_graph)

            for value in scores.values():
                print(value, end=" ")

            print()
