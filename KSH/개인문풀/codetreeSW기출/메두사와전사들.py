'''

1. 반드시 단계별로 디버깅
2. 문제 중간에 엣지/최대/극단 케이스 넣어보기
3. 멍 때리지 말기
4. 조건 빼먹는 것, 문제 똑바로 읽는 것 주의







'''


from collections import deque


### 1. 집까지 최단 경로 찾기
'''
도로는 0, 도로 아닌 곳 1

        house_x, house_y, park_x, park_y = list(map(int, input().split())) # 메두사 집, 공원 좌표
        warrior_input = list(map(int, input().split()))

        warriors = [] # 전사 좌표 리스트
        town_graph = [] # 마을

'''
def shortest_path(town_graph, info_list):

    house_x, house_y, park_x, park_y = info_list # 집 좌표와 공원 좌표 할당

    q = deque()
    q.append([house_x, house_y])
    # visited[house_x][house_y] = True

    dx = [-1, 1, 0, 0] # 상,하,좌,우 순서
    dy = [0, 0, -1, 1]

    visited = [[0] * n for _ in range(n)]
    visited[house_x][house_y] = True

    dist_graph = [[3000] * n for _ in range(n)]
    dist_graph[house_x][house_y] = 0

    while q:
        cx, cy = q.popleft()
        flag = 0

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx == park_x and ny == park_y:
                flag = 1
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and town_graph[nx][ny] != 1:
                visited[nx][ny] = True

                distance = dist_graph[cx][cy] + 1
                if distance < dist_graph[nx][ny]:
                    dist_graph[nx][ny] = distance

                q.append([nx, ny])

        if flag: # 공원에 도착했다면, bfs 종료하기
            break

    if dist_graph[park_x][park_y] == 3000:
        return False, dist_graph
    else:
        return True, dist_graph



### 2. 메두사 이동하기
def move_medusa(info_list, dist_graph):
    house_x, house_y, park_x, park_y = info_list

    now_distance = 0 # 현재 거리

    medusa_x = house_x
    medusa_y = house_y

    direction = [[-1,0],[1,0],[0,-1],[0,1]] # 움직일 수 있는 방향

    while True:
        for dx, dy in direction:
            moved_medusa_x = house_x + dx
            moved_medusa_y = house_y + dy
            if dist_graph[moved_medusa_x][moved_medusa_y] == (now_distance + 1): # 만일 메두사가 움직인 곳이 최단거라면






### 3. 메두사 시선 선택

# def medusa_sight



### 4. 전사 이동하기




### 5. 전사 공격하기




if __name__ == "__main__":

    t = int(input())

    for _ in range(t):
        n, m = list(map(int, input().split())) # 마을 크기 n, 전사수 m

        info_list = list(map(int, input().split())) # 메두사 집, 공원 좌표
        # house_x, house_y, park_x, park_y = info_list
        warrior_input = list(map(int, input().split()))

        warriors = [] # 전사 좌표 리스트
        town_graph = [] # 마을

        for k in range(m):
            warriors.append([warrior_input[2*k], warrior_input[2*k+1]])

        for i in range(n):
            town_graph.append(list(map(int, input().split())))

        road_flag, dist_graph = shortest_path(town_graph, info_list)

        if road_flag:
            for i in range(n):
                print(dist_graph[i])
            print("Good")










