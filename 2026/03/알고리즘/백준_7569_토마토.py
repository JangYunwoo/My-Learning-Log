from collections import deque

M, N, H = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

day = -1
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
q = deque()
count = 0


for h in range(H):
    for r in range(N):
        for c in range(M):
            if tomato_box[h][r][c] == 1:
                q.append([h, r, c])
            elif tomato_box[h][r][c] == 0:
                count += 1

while q:
    day += 1
    for _ in range(len(q)):
        h, x, y = q.popleft()
        for dir in range(6):
            nh = h + dh[dir]
            nx = x + dr[dir]
            ny = y + dc[dir]
            if 0 <= nx < N and 0 <= ny < M and 0<=nh<H and tomato_box[nh][nx][ny] == 0:
                q.append([nh, nx, ny])
                tomato_box[nh][nx][ny] = 1
                count -= 1

if count == 0:
    print(day)
else:
    print(-1)