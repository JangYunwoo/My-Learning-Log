from collections import deque

N, M, K = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque([[0, 0, 0]])
count = 1
while q:
    count += 1
    for _ in range(len(q)):
        x, y, w = q.popleft()
    
        for dir in range(4):
            nx = x+dr[dir]
            ny = y+dc[dir]

            if 0<=nx<N and 0<=ny<M:

                if graph[nx][ny] == 1 and w < K:
                    if visited[nx][ny] > w-1 or visited[nx][ny] == -1:
                        nw = w+1
                        visited[nx][ny] = nw
                        q.append([nx, ny, nw])
                elif graph[nx][ny] == 0:
                    if visited[nx][ny] > w or visited[nx][ny] == -1:
                        visited[nx][ny] = w
                        q.append([nx, ny, w])
    if  visited[N-1][M-1] != -1:
        print(count)
        break
    
else:
    print(-1)