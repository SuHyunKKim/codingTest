'''




'''
from collections import deque, defaultdict

### 그래프 확인 함수
def see_my_graph(graph):

    for i in range(len(graph)):
        print(graph[i])

def find_exit(gs_x, gs_y, direction):

    if direction == 0:
        exit_x, exit_y = gs_x-2, gs_y
    elif direction == 1:
        exit_x, exit_y = gs_x-1, gs_y+1
    elif direction == 2:
        exit_x, exit_y = gs_x, gs_y
    else:
        exit_x, exit_y = gs_x-1, gs_y-1

    return exit_x, exit_y

def bfs(golum_exit_south_info, forest_graph, golum_num):

    gs_x, gs_y, direction = golum_exit_south_info[golum_num]
    exit_x, exit_y = find_exit(gs_x, gs_y, direction)
    ### 출구 좌표 찾기

    max_depth = -1
    if gs_x > max_depth:
        max_depth = gs_x + 1

    visited = [[0] * c for _ in range(r)]

    q = deque()
    q.append([exit_x, exit_y, golum_num])
    visited[exit_x][exit_y] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        now_exit_x, now_exit_y, golum_num = q.popleft()
        for i in range(4):
            nx = now_exit_x + dx[i]
            ny = now_exit_y + dy[i]
            # 만일 그래프 내고, 0 이 아니고 골름이고,
            if 0<=nx<r and 0<=ny<c and forest_graph[nx][ny] != 0:
                golum_sx, golum_sy, direction = golum_exit_south_info[forest_graph[nx][ny]]
                if not visited[golum_sx][golum_sy]: # 만일 방문 안한 골름이면

                    if golum_sx + 1 > max_depth:    # 골름 최대 깊이 업데이트
                        max_depth = golum_sx + 1

                    now_exit_x, now_exit_y = find_exit(golum_sx, golum_sy, direction)

                    q.append([now_exit_x, now_exit_y, forest_graph[nx][ny]])
                    visited[golum_sx][golum_sy] = True

    return max_depth

def move_golum(forest_graph, golum_start_exit_info):
    golum_exit_south_info = defaultdict(list)
    golum_num = 1
    depth_sum = 0

    for g in golum_start_exit_info:

        move_finish = 0

        golum_start = g[0]      # 골름 시작 위치
        golum_exit = g[1]       # 골름 출구 번호

        # 골름 좌표들
        golum_south = [-1, golum_start]
        # 골름 남쪽 x와 y 좌표
        gs_x, gs_y = golum_south[0], golum_south[1]


        ''' 첫번째 움직임 '''
        if forest_graph[0][gs_y] == 0:
            gs_x += 1
            # golum_west[0] += 1
            # golum_east[0] += 1
            # golum_north[0] += 1

        elif gs_y-1>=1 and forest_graph[0][gs_y-1] == 0:
            gs_x += 1 # 골름 밑으로 한칸 이동
            gs_y -= 1 # 골름 서쪽 한칸 이동
            golum_exit = (golum_exit - 1) % 4

        elif gs_y+1<=c-2 and forest_graph[0][gs_y+1] == 0:
            gs_x += 1  # 골름 밑으로 한칸 이동
            gs_y += 1  # 골름 동쪽 한칸 이동
            golum_exit = (golum_exit + 1) % 4

        else:
            move_finish = 1

        if move_finish:
            forest_graph = [[0] * c for _ in range(r)]
            continue

        ''' 두, 세번째 움직임 '''
        ### gs_x, gs_y = golum_south[0], golum_south[1]
        # 남: forest_graph[gs_x][gs_y]
        # 서: forest_graph[(gs_x-1)][(gs_y-1)]
        # 동: forest_graph[(gs_x-1)][(gs_y+1)]
        # 북: forest_graph[(gs_x-2)][gs_y]

        if forest_graph[gs_x+1][gs_y] == 0 and forest_graph[(gs_x-1)+1][(gs_y-1)] == 0 and forest_graph[(gs_x-1)+1][(gs_y+1)] == 0:
            gs_x += 1
        elif (gs_y-1)>=1 and forest_graph[gs_x][gs_y-1] == 0 and forest_graph[(gs_x-1)+1][(gs_y-1)-1] == 0 and forest_graph[gs_x+1][gs_y-1] == 0:
                gs_x += 1
                gs_y -= 1
                golum_exit = (golum_exit - 1) % 4
        elif (gs_y+1)<=c-2 and forest_graph[gs_x][gs_y+1] == 0 and forest_graph[(gs_x-1)+1][(gs_y+1)+1] == 0 and forest_graph[gs_x+1][gs_y+1] == 0:
                gs_x += 1
                gs_y += 1
                golum_exit = (golum_exit + 1) % 4
        else:
            move_finish = 1

        if move_finish:
            forest_graph = [[0] * c for _ in range(r)]
            continue

        ''' 세번째 움직임 '''
        if forest_graph[gs_x+1][gs_y] == 0 and forest_graph[(gs_x-1)+1][(gs_y-1)] == 0 and forest_graph[(gs_x-1)+1][(gs_y+1)] == 0:
            gs_x += 1
        elif (gs_y-1)>=1 and forest_graph[(gs_x-1)][(gs_y-1)-1] == 0 and forest_graph[gs_x][gs_y-1] == 0 and forest_graph[(gs_x-1)+1][(gs_y-1)-1] == 0 and forest_graph[gs_x+1][gs_y-1] == 0:
                gs_x += 1
                gs_y -= 1
                golum_exit = (golum_exit - 1) % 4
        elif (gs_y+1)<=c-2 and forest_graph[(gs_x-1)][(gs_y+1)+1] == 0 and forest_graph[gs_x][gs_y+1] == 0 and forest_graph[(gs_x-1)+1][(gs_y+1)+1] == 0 and forest_graph[gs_x+1][gs_y+1] == 0:
                gs_x += 1
                gs_y += 1
                golum_exit = (golum_exit + 1) % 4
        else:
            move_finish = 1

        if move_finish:
            forest_graph = [[0] * c for _ in range(r)]
            continue

        ''' 그 이후 움직임 '''
        while True:
            ### 종료 조건 교훈
            if gs_x > r-2 or move_finish:
                move_finish = 2
                break

            if forest_graph[gs_x + 1][gs_y] == 0 and forest_graph[(gs_x - 1) + 1][(gs_y - 1)] == 0 and forest_graph[(gs_x - 1) + 1][(gs_y + 1)] == 0:
                gs_x += 1
            elif ((gs_y - 1) >= 1 and forest_graph[(gs_x - 1)][(gs_y - 1) - 1] == 0 and forest_graph[gs_x][gs_y - 1] == 0 and forest_graph[(gs_x-2)][gs_y - 1] == 0
                  and forest_graph[(gs_x - 1) + 1][(gs_y - 1) - 1] == 0 and forest_graph[gs_x + 1][gs_y - 1] == 0):
                    gs_x += 1
                    gs_y -= 1
                    golum_exit = (golum_exit - 1) % 4
            elif ((gs_y + 1) <= c - 2 and forest_graph[(gs_x - 1)][(gs_y + 1) + 1] == 0 and forest_graph[gs_x][gs_y + 1] == 0 and forest_graph[(gs_x-2)][gs_y + 1] == 0
                  and forest_graph[(gs_x - 1) + 1][(gs_y + 1) + 1] == 0 and forest_graph[gs_x + 1][gs_y + 1] == 0):
                    gs_x += 1
                    gs_y += 1
                    golum_exit = (golum_exit + 1) % 4
            else:
                move_finish = 2

        # move_finish = 2

        if move_finish == 2:
            for x,y in [[gs_x,gs_y], [gs_x-1,gs_y-1], [gs_x-1,gs_y+1], [gs_x-2,gs_y], [gs_x-1,gs_y]]:
                forest_graph[x][y] = golum_num


        golum_exit_south_info[golum_num] = [gs_x, gs_y, golum_exit]

        max_depth = bfs(golum_exit_south_info, forest_graph, golum_num)
        depth_sum += max_depth

        golum_num += 1  # 골름 번호를 다르게 하기 위함임

    # see_my_graph(forest_graph)

    return forest_graph, depth_sum


if __name__ == "__main__":

    file = open("./test2.txt")
    T = int(file.readline())

    for _ in range(T):
        # r : 행, c: 열, k : 정령수
        r, c, k = list(map(int, file.readline().split()))

        forest_graph = [[0] * c for _ in range(r)]          # 숲 그래프

        golum_start_exit_info = []                          # 골름 시작 열, 출구 정보 (북, 동, 남, 서)
        for _ in range(k):
            start, golum_exit = list(map(int, file.readline().split()))
            start -= 1
            golum_start_exit_info.append([start, golum_exit])

        new_forest_graph, depth_sum = move_golum(forest_graph, golum_start_exit_info)

        print(depth_sum)

    print()