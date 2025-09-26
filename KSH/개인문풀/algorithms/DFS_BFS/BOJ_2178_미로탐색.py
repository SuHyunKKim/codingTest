'''






'''
from collections import deque

def my_print(graph):

    for i in range(n):
        print(graph[i])


def bfs(graph):

    route_graph = [[0] * m for _ in range(n)]

    q = deque()
    q.append([0,0])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    # direction = 1

    while q:
        cx, cy = q.popleft()

        if cx == n-1 and cy == m-1: # 만일 n,m에 도달했다면
            route = [[cx, cy]]
            cx, cy = route_graph[cx][cy]
            while True:

                route.append([cx, cy])
                cx, cy = route_graph[cx][cy]
                if cx == 0 and cy == 0:
                    break
            route.append([0,0])

            return len(route), route[::-1]

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<n and 0<=ny<m and not route_graph[nx][ny] and graph[nx][ny] == 1:
                q.append([nx, ny])
                route_graph[nx][ny] = [cx,cy]


    return False

if __name__ == "__main__":

    f = open('./tc.txt')
    t = int(f.readline())
    print(t)

    for k in range(t):
        n, m = list(map(int, f.readline().split()))

        graph = []

        for i in range(n):
            graph.append(list(map(int,  f.readline().rstrip())))

        # print(graph)

        direction, route = bfs(graph)
        print(f'#{k+1} {direction}')


'''

    n, m = list(map(int, input().split()))

    graph = []

    for i in range(n):
        graph.append(list(map(int, input())))

    # print(graph)

    direction, route = bfs(graph)
    print(direction)
    # print(route)



    # print()

'''





