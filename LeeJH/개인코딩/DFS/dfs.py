
#dfs는 스택을 이용한 깊이 우선 탐색 알고리즘이다.
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph= [
    [], #0번째 Index
    [2,3,8], #1번 Index와 인접한 노드
    [1,7], #2번 Index와 인접한노드
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

#정의된 DFS 함수 호출
dfs(graph, 1, visited)

#결과 : 1 2 7 6 8 3 4 5