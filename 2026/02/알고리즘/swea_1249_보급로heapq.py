import heapq

dr = [-1,1,0,0]
dc = [0,0,-1,1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[float('inf')]*N for _ in range(N)]

    hq = []
    heapq.heappush(hq, (0,0,0))
    visited[0][0] = 0

    while hq:
        s, x, y = heapq.heappop(hq)

        if x == N-1 and y == N-1:
            print(f"#{tc} {s}")
            break

        if s > visited[x][y]:
            continue

        for dir in range(4):
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<N and 0<=ny<N:
                if s+board[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = s+board[nx][ny]
                    heapq.heappush(hq, (s+board[nx][ny], nx, ny))