from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque([[0, 0, 0]])
visited[0][0][0] = 1

while q:
    x, y, w = q.popleft()

    if x == N-1 and y == M-1:
        print(visited[x][y][w])
        exit()

    for dir in range(4):
        nx = x+dr[dir]
        ny = y+dc[dir]

        if 0<=nx<N and 0<=ny<M:

            if graph[nx][ny] == 1 and w == 0:
                if visited[nx][ny][1] == 0:
                    visited[nx][ny][1] = visited[x][y][w] + 1
                    q.append([nx, ny, 1])
            elif graph[nx][ny] == 0:
                if visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append([nx, ny, w])

else:
    print(-1)