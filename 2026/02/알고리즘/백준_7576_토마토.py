import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

tomato_box = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

day = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
q = deque()

while True:
    count = 0
    for r in range(N):
        for c in range(M):
            if tomato_box[r][c] == 1 and visited[r][c] == 0:
                visited[r][c] = 1
                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]
                    if 0 <= nr < N and 0 <= nc < M and tomato_box[nr][nc] == 0:
                        q.append([nr, nc])
                        count += 1

    if count == 0:
        break

    for _ in range(len(q)):
        x, y = q.popleft()
        tomato_box[x][y] = 1

    day += 1

for r in range(N):
    for c in range(M):
        if tomato_box[r][c] == 0:
            print(-1)
            exit()

print(day)