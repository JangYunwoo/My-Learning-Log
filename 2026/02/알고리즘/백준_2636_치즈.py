from collections import deque

N, M = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

hour = 0
visited[0][0] = 1

q = deque([[0, 0]])
new_q = deque()

count = 0
for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            count += 1

while q:
    hour += 1
    for _ in range(len(q)):
        r, c = q.popleft()
        for dir in range(4):
            nr = r+dr[dir]
            nc = c+dc[dir]
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if graph[nr][nc] == 0:
                    new_q.append([nr, nc])
                    while new_q:
                        for _ in range(len(new_q)):
                            r2, c2 = new_q.popleft()
                            for dir2 in range(4):
                                nr2 = r2+dr[dir2]
                                nc2 = c2+dc[dir2]
                                if 0<=nr2<N and 0<=nc2<M and visited[nr2][nc2] == 0:
                                    if graph[nr2][nc2] == 0:
                                        new_q.append([nr2, nc2])
                                        visited[nr2][nc2] = 1
                                    else:
                                        q.append([nr2, nc2])
                                        visited[nr2][nc2] = 1
                                        graph[r][c] = 0
                else:
                    q.append([nr, nc])
                    visited[nr][nc] = 1
                    graph[r][c] = 0
    count -= len(q)
    if count == 0:
        print(hour)
        print(len(q))
        break

# 1. 테두리 감지 > 치즈 바깥쪽에서 bfs / dfs
# 2. 감지된 테두리를 삭제