from collections import deque
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dr = [-1, 1, 0, 0, 1, 1, 2, 2, -1, -1, -2, -2]
dc = [0, 0, -1, 1, 2, -2, 1, -1, 2, -2, 1, -1]
q = deque([[0, 0, 1]])
count = 0

while q:
    count += 1
    for i in range(len(q)):
        r, c, h = q.popleft()
        for dir in range(12 if h < K+1 else 4):
            nr = r+dr[dir]
            nc = c+dc[dir]
            if dir >=4:
                nh = h+1
            else:
                nh = h
            if 0<=nr<H and 0<=nc<W and board[nr][nc] != 1:
                if board[nr][nc] > nh or board[nr][nc] == 0:
                    board[nr][nc] = nh
                    q.append([nr, nc, nh])

    if board[H-1][W-1] != 0:
        print(count)
        break

else:
    print(-1)