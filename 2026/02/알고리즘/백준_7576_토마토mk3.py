import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

q = deque()
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 시작점 전부 큐에 박아넣기
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j, 0))

day = 0

while q:
    x, y, day = q.popleft()
    for d in range(4):
        nx = x + dr[d]
        ny = y + dc[d]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            box[nx][ny] = 1
            q.append((nx, ny, day + 1))

# 안 익은 거 남았는지 검사
for row in box:
    if 0 in row:
        print(-1)
        sys.exit()

print(day)
