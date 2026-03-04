from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
wall = []
street = []
route = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            wall.append([r, c])
        else:
            street.append([r, c])

for a, b in wall:
    q = deque([[0, 0]])
    graph[0][0] = 2
    graph[a][b] = 0
    count = 1

    while q:
        count += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dir in range(4):
                nx = x+dr[dir]
                ny = y+dc[dir]
                if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0:
                    q.append([nx, ny])
                    graph[nx][ny] = 2

        if graph[N-1][M-1] == 2:
            route.append(count)
            break
    
    graph[a][b] = 1
    for c, d in street:
        graph[c][d] = 0

if route:
    print(min(route))
else:
    print(-1)