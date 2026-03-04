from collections import deque

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    q = deque()
    visited = [[0]*N for _ in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    monster = []

    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                for dir in range(4):
                    nr = r+dr[dir]
                    nc = c+dc[dir]
                    if 0<=nr<N and 0<=nc<N and board[nr][nc] == 0:
                        q.append([nr, nc])
                        count -= 1
                        while q:
                            a, b = q.popleft()
                            na = a+dr[dir]
                            nb = b+dc[dir]
                            if 0<=na<N and 0<=nb<N and board[na][nb] == 0:
                                q.append([na, nb])
                                count -= 1
            elif board[r][c] == 0:
                count += 1

    print(f"#{tc} {count}")
        
    