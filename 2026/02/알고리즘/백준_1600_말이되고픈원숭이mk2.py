from collections import deque
K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]

dr = [-1, 1, 0, 0, 1, 1, 2, 2, -1, -1, -2, -2]
dc = [0, 0, -1, 1, 2, -2, 1, -1, 2, -2, 1, -1]
q = deque([[0, 0, 0]])
visited = [[[0]*W for _ in range(H)] for _ in range(K+1)]
visited[0][0][0] = 1
count = 0

while q:
    for i in range(len(q)):
        h, r, c = q.popleft()

        if r == H-1 and c == W-1:
            print(count)
            exit()

        for dir in range(12 if h < K else 4):
            nr = r+dr[dir]
            nc = c+dc[dir]
            if dir >=4:
                nh = h+1
            else:
                nh = h
            if 0<=nr<H and 0<=nc<W and board[nr][nc] == 0 and visited[nh][nr][nc] == 0:
                visited[nh][nr][nc] = 1
                q.append([nh, nr, nc])

    count += 1
    
else:
    print(-1)