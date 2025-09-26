

from collections import deque

def bfs(start, target, graph):

    visited = [0] * (n+1)

    q = deque()
    q.append([start, 0])
    visited[start] = True

    while q:
        cur, relation = q.popleft()

        if cur == target: # 종료 조건
            return relation

        for nex in graph[cur]:
            if nex and not visited[nex]:
                visited[nex] = True
                q.append([nex, relation+1])

    return False



if __name__ == "__main__":

    n = int(input())

    start, target = list(map(int, input().split()))  # 촌수 관계 구해야되는 시작과 대상

    m = int(input())

    graph = [[0] for _ in range(n + 1)]

    for k in range(m):
        x, y = list(map(int, input().split()))
        graph[x].append(y)
        graph[y].append(x)

    ans = bfs(start, target, graph)

    if n == 1 or m == 0:
        print(-1)
    elif not ans:
        print(-1)
    else:
        print(ans)

'''
    f = open('./tc.txt')

    T = int(f.readline())

    for i in range(T):
        n = int(f.readline()) # 사람 수

        if n == 1:
            print(-1)
            continue

        start, target = list(map(int, f.readline().split())) # 촌수 관계 구해야되는 시작과 대상

        m = int(f.readline()) # 관계 수

        if m == 0:
            print(-1)
            continue

        graph = [[0] for _ in range(n+1)]

        for k in range(m):
            x, y = list(map(int, f.readline().split()))
            graph[x].append(y)
            graph[y].append(x)

        ans = bfs(start, target, graph)

        if not ans:
            print(-1)
        else:
            print(ans)
'''
