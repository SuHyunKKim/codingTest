'''

접근 방식
- 한칸한칸 일일히 접근해야할 듯
- 걸려있는 조건에 따라 분기해야할 듯

풀이 순서
- 미세먼지 확산을 모든 칸 별로 계산
    - 겹치는 칸이 있다
    - 공기청정기가 있는 칸이 있다
    - 막혀있는 칸이 있다

- 확산 후, 확산된 양만큼 빼줘야한다

- 공기청정기 순환을 계산
    - 위는 반시계
    - 아래는 시계

----------------------
틀린 부분
- 얕은 복사

'''
import sys


### 1. 입력 받기
r,c,t = list(map(int, sys.stdin.readline().split()))

graph = [[0]] * r
# 실수 포인트
# graph_sub = [[0] * c] * r # 원본을 훼손하지 않을 sub 그래프
graph_sub = [[0] * c for _ in range(r)] # 원본을 훼손하지 않을 sub 그래프
graph_new = [[0] * c for _ in range(r)]
for i in range(r):
    graph[i] = list(map(int, sys.stdin.readline().split()))

### 2. 미세먼지 확산

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cleaner = []

for row in range(r):
    for col in range(c):

        if graph[row][col] == -1:
            graph_sub[row][col] = -1
            cleaner.append(row)
            cleaner.append(col)
            continue

        if graph[row][col] >= 5:
            spread = graph[row][col] // 5
            count = 0
            for i in range(4):
                nx = row + dx[i]
                # 실수 포인트 - 미친 오타..
                # ny = row + dy[i]
                ny = col + dy[i]
                if 0<=nx<r and 0<=ny<c: # 좌표가 아니라 행,열 이기 때문에 nx는 r, ny는 c로 검사하는 것임.
                    if graph[nx][ny] != -1:
                        graph_sub[nx][ny] += spread
                        count += 1
            # 실수 포인트 - 이전 단계에서 업데이트 된 sub 그래프 값을 더해주고 시작해야되는데 그러지 못함
            graph_sub[row][col] = graph_sub[row][col] + graph[row][col] - (spread * count)
            # or.. graph_sub[row][col] += graph[row][col] - (spread * count)

print(graph_sub)
print(cleaner)

### 3. 공기청정기 작동
ux, uy, dx, dy = cleaner
# 그래프를 새로 할당하면, 순환 된 것 외에 가만히 있는 먼지도 다 다시 할당 해줘야함
# 그래서 바
for i in range(uy, 1, -1):
    graph_sub[ux][i] = graph_sub[ux][i-1]

# graph[ux][uy] = 0

for i in range(ux, 1, -1):
    graph_sub[i][0] = graph_sub[i-1][0]

for i in range(0, uy):
    graph_sub[0][i] = graph_sub[0][i+1]

for i in range(0, ux):
    graph_sub[i][c-1] = graph_sub[i+1][c-1]

for i in range(c-1, uy+1, -1):
    graph_sub[ux][i] = graph_sub[ux][i-1]

graph_sub[ux][uy] = -1