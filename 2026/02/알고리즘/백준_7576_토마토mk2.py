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

for r in range(N):
        for c in range(M):
            if tomato_box[r][c] == 1 and visited[r][c] == 0:
                q.append([r, c])

while True:
    count = 0
    for _ in range(len(q)):
        x, y = q.popleft()
        visited[x][y] = 1
        for dir in range(4):
            nx = x + dr[dir]
            ny = y + dc[dir]
            if 0 <= nx < N and 0 <= ny < M and tomato_box[nx][ny] == 0:
                q.append([nx, ny])
                tomato_box[nx][ny] = 1
                count = 1

    if count == 0:
        break
    day += 1

for r in range(N):
    for c in range(M):
        if tomato_box[r][c] == 0:
            print(-1)
            exit()

print(day)