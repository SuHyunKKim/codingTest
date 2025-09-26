'''

출구와 출구 방향 찾기
시간 벽 그래프 입력 받기
시간 벽 그래프 plot 하기 - bfs를 위해






'''
from collections import deque



def print_graph(graph):

    for i in range(len(graph)):
        print(graph[i])


### 1. 시간의 벽 출구 좌표 찾는 함수 - 출구와 출구 방향 찾기
def find_exit(unknown_space):

    surround = [] # 시간의 벽 둘러싸는 좌표
    exit = []

    for i in range(n): # while 문으로 바꾸는게 더 깔끔할듯.
        flag = 0
        for j in range(n):
            if unknown_space[i][j] == 3:
                surround.append([i-1, j-1])
                surround.append([i+m, j+m])
                flag = 1 # 반복문 종료 조건
                break
        if flag:
            break

    [sx, sy], [ex, ey] = surround

    flag2 = 0 # while 문 멈추기 위한 flag

    for i in range(sx, ex+1):
        for j in range(sy, ey+1):
            if unknown_space[i][j] == 0:
                exit.append(i)
                exit.append(j)
                flag2 = 1
                break
        if flag2:
            break
    # print(exit)
    ## exit = 출구 x,y좌표, 아래서 출구 방향 동/서/남/북으로 ㅊ자기
    exit_direction = -1

    if exit[1] == ey:
        exit_direction = 0
    elif exit[1] == sy:
        exit_direction = 1
    elif exit[0] == ex:
        exit_direction = 2
    else:
        exit_direction = 3


    return surround, exit, exit_direction

def plot_time_graphs():

    east_graph = []
    west_graph = []
    south_graph = []
    north_graph = []
    mid_graph = []

    for i in range(5 * m):
        if i < m:
            east_graph.append(list(map(int, file.readline().split())))
        elif m <= i < 2 * m:
            west_graph.append(list(map(int, file.readline().split())))
        elif m <= i < 3 * m:
            south_graph.append(list(map(int, file.readline().split())))
        elif m <= i < 4 * m:
            north_graph.append(list(map(int, file.readline().split())))
        else:
            mid_graph.append(list(map(int, file.readline().split())))

    return east_graph, west_graph, south_graph, north_graph, mid_graph

## 시간 벽 총체 그래프 만들기
def make_time_graph(unknown_graph, exit_loc, exit_direction, *graphs):
    e_g, w_g, s_g, n_g, m_g = graphs

    time_wall = [[1] * (3*m+2) for _ in range(3*m+2)]
    time_machine_loc = []

    # 0이 빈공간, 1이 벽, 2가 타임머신, 5를 자유 출입 가능 그러나 길이에 추가 안하는 걸로 바꾸자
    # 1. 자유 출입 공간 만들기
    for i in range(1, 3*m+1):
        for j in range(1, 3*m+1):
            time_wall[i][j] = 5

    # 2. 동서남북, 중앙 plot
    for i in range(m+1, 2*m+1): # 중앙
        for j in range(m+1, 2*m+1):
            time_wall[i][j] = m_g[i-(m+1)][j-(m+1)]
            if time_wall[i][j] == 2:
                time_machine_loc = [i,j]

    for i in range(2*m+1, 3*m+1): # 남
        for j in range(m+1, 2*m+1):
            time_wall[i][j] = s_g[i-(2*m+1)][j-(m+1)]

    rotate_e_g = [[0] * m for _ in range(m)] # 동
    for i in range(m):
        for j in range(m):
            rotate_e_g[i][j] = e_g[j][m-1-i]

    for i in range(m+1, 2*m+1):
        for j in range(2*m+1, 3*m+1):
            time_wall[i][j] = rotate_e_g[i-(m+1)][j-(2*m+1)]

    rotate_n_g = [[0] * m for _ in range(m)] # 북
    for i in range(m):
        for j in range(m):
            rotate_n_g[i][j] = n_g[m-1-i][m-1-j]

    for i in range(1, m+1):
        for j in range(m+1, 2*m+1):
            time_wall[i][j] = rotate_n_g[i-1][j-(m+1)]

    rotate_w_g = [[0] * m for _ in range(m)] # 서
    for i in range(m):
        for j in range(m):
            rotate_w_g[j][m-1-i] = w_g[i][j]

    for i in range(m+1, 2*m+1):
        for j in range(1, m+1):
            time_wall[i][j] = rotate_w_g[i-(m+1)][j-1]

    [sx, sy], [ex, ey] = surround
    # 3. 출구 부분
    exit_target = []

    if exit_direction == 0:
        j = exit_loc[1]
        for i in range(sx, ex+1):
            time_wall[m+i-sx][3*m+1] = unknown_graph[i][j]
            if time_wall[m+i-sx][3*m+1] == 0:
                exit_target = [m+i-sx, 3*m+1]
    elif exit_direction == 1:
        j = exit_loc[1]
        for i in range(sx, ex+1):
            time_wall[m+i-sx][1] = unknown_graph[i][j]
            if time_wall[m+i-sx][1] == 0:
                exit_target = [m+i-sx, 1]
    elif exit_direction == 2:
        i = exit_loc[0]
        for j in range(sy, ey+1):
            time_wall[3*m+1][m+j-sy] = unknown_graph[i][j]
            if time_wall[3*m+1][m+j-sy] == 0:
                exit_target = [3*m+1, m+j-sy]
    elif exit_direction == 3:
        i = exit_loc[0]
        for j in range(sy, ey+1):
            time_wall[1][m+j-sy] = unknown_graph[i][j]
            if time_wall[1][m+j-sy] == 0:
                exit_target = [1, m+j-sy]

    # print_graph(time_wall)

    return time_wall, time_machine_loc, exit_target

def bfs(time_wall, time_machine_loc, exit_target):

    N = len(time_wall)
    # print(exit_target)

    visited = [[0] * N for _ in range(N)]
    new_time_machine_loc = time_machine_loc + [0]

    q = deque()
    q.append(new_time_machine_loc)

    visited[time_machine_loc[0]][time_machine_loc[1]] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        cx, cy, distance = q.popleft()

        if cx == exit_target[0] and cy == exit_target[1]:
            return distance + 1

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and time_wall[nx][ny] != 1:
                visited[nx][ny] = True
                if time_wall[nx][ny] == 5:
                    q.append([nx, ny, distance])
                else:
                    q.append([nx, ny, distance+1])

    return False

def bfs_unknown_graph(unknown_graph, distance, situation, exit_loc):

    for s in situation:
        s_x, s_y = s[0], s[1]
        unknown_graph[s_x][s_y] = 7


    visited = [[0] * n for _ in range(n)]

    new_exit_loc = exit_loc + [distance]

    q = deque()
    q.append(new_exit_loc)

    visited[new_exit_loc[0]][new_exit_loc[1]] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    turn = distance

    while q:
        cx, cy, now_dist = q.popleft()
        # print(cx, cy, now_dist)
        if cx == real_exit[0] and cy == real_exit[1]:
            return now_dist
        now_dist += 1
        # print(turn, now_dist)
        if turn != now_dist:
            turn = now_dist

            for s in situation:
                s_x, s_y = s[0], s[1]
                direction = s[2]
                v = s[3]

                if turn % v == 0: # 만일 나머지가 0이면
                    if direction == 0:
                        s_y += 1
                        if 0<= s_y < n-1 and unknown_graph[s_x][s_y] == 0:
                            unknown_graph[s_x][s_y] = 7
                            s[1] = s_y
                    elif direction == 1:
                        s_y -= 1
                        if 0< s_y < n and unknown_graph[s_x][s_y] == 0:
                            unknown_graph[s_x][s_y] = 7
                            s[1] = s_y
                    elif direction == 2:
                        s_x += 1
                        if 0 <= s_x < n-1 and unknown_graph[s_x][s_y] == 0:
                            unknown_graph[s_x][s_y] = 7
                            s[0] = s_x
                    elif direction == 3:
                        s_x -= 1
                        if 0 < s_x <= n-1 and unknown_graph[s_x][s_y] == 0:
                            unknown_graph[s_x][s_y] = 7
                            s[0] = s_x

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and (unknown_graph[nx][ny] == 0 or unknown_graph[nx][ny] == 4):
                visited[nx][ny] = True
                q.append([nx,ny,now_dist])

    # print_graph(unknown_graph)

    return False


if __name__ == "__main__":

    file = open("./test_case.txt")

    T = int(file.readline())

    for _ in range(T):
        '''입력 받기'''

        n, m, f = list(map(int, file.readline().split())) # n 미지 공간 크기, m 시간 벽 한 단면 크기, f 이상 현상 갯수

        ### 미지 공간 입력 받기
        unknown_space = []          # 미지의 공간 그래프
        for _ in range(n):
            unknown_space.append(list(map(int, file.readline().split())))

        real_exit = []
        for i in range(n):
            for j in range(n):
                if unknown_space[i][j] == 4:
                    real_exit = [i,j]
            if real_exit:
                break

        # print(real_exit)
        ### 시간의 벽들 입력 받기
        e_g, w_g, s_g, n_g, m_g = plot_time_graphs()

        ### 이상 상황 입력 받기
        situation = []
        for _ in range(f):
            situation.append(list(map(int, file.readline().split())))

        '''기능 수행'''

        surround, exit_loc, exit_direction = find_exit(unknown_space) # 둘러쌓는 좌표와 출구 시간 벽 출구 좌표 리턴

        ### time_wall : 시간의 벽 bfs 할 것
        time_wall, time_machine_loc, exit_target = make_time_graph(unknown_space, exit_loc, exit_direction, e_g, w_g, s_g, n_g, m_g)
        ### 시간의 벽 bfs
        # print_graph(time_wall)

        distance = bfs(time_wall, time_machine_loc, exit_target)
        if not distance:
            print(-1)
            continue

        final_distance = bfs_unknown_graph(unknown_space, distance, situation, exit_loc)

        # print(distance)
        print(final_distance)


    print()





