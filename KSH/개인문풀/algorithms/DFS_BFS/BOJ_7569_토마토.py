'''


- bfs로 풀기

1. 3차원 배열에 토마토 상자 할당하기
2. 토마토 모두 익었는지 검사
3. bfs로 근접한 토마토 익히기
4. 안익은 토마토가 있는지 검사

'''


### 1. 입력 받기

import sys
from collections import deque

# n - 열, m - 행, h - 높이
n, m, h = list(map(int, sys.stdin.readline().split()))


# 토마토 상자
tomato_boxes = [[[0] * n for _ in range(m)] for _ in range(h)]

for i in range(h):
    for k in range(m):
        tomato_boxes[i][k] = list(map(int, sys.stdin.readline().split()))

# print(tomato_boxes)

next_tomato = [[1,0,0], [-1,0,0],
               [0,1,0], [0,-1,0],
               [0,0,1], [0,0,-1]]

def check_all_ripe(tomato_boxes):

    flag = 0
    for a in range(h):
        for b in range(m):
            for c in range(n):
                if not tomato_boxes[a][b][c]:
                    flag = 1
                    break
            if flag:
                break
        if flag:
            break

    return flag

def bfs(tomato_boxes, visited):

    flag = check_all_ripe(tomato_boxes)
    if not flag: # flag가 0으로 이미 다 익었다면
        return 0, 0
    # 날짜

    # 익은 토마토가 담길 queue
    q = deque()

    # 마지막 토마토
    last_tomato_day = -1

    for a in range(h):
        for b in range(m):
            for c in range(n):
                if tomato_boxes[a][b][c] == 1: # 이거 if tomato_boxes[a][b][c]: 로 하면 -1도 인식 되버림
                    q.append((a,b,c,0))
                    visited[a][b][c] = True

    while q:
        cz, cy, cx, today = q.popleft() # 현재 토마토
        last_tomato_day = today
        for i in range(6):
            nz = cz + next_tomato[i][0]
            ny = cy + next_tomato[i][1]
            nx = cx + next_tomato[i][2]
            if 0<=nz<h and 0<=ny<m and 0<=nx<n and not visited[nz][ny][nx]:
                if not tomato_boxes[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    tomato_boxes[nz][ny][nx] = 1
                    q.append((nz, ny, nx, today+1))

    return tomato_boxes, last_tomato_day


visited = [[[0] * n for _ in range(m)] for _ in range(h)]
new_tomato_boxes, min_day = bfs(tomato_boxes, visited)

if not min_day: # 만일 처음부터 다 익었었다면
    print(0)
else:
    if check_all_ripe(new_tomato_boxes):
        print(-1)
    else:
        print(min_day)

# print(new_tomato_boxes, min_day)
