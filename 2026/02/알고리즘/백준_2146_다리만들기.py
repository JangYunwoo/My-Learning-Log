from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

grounds = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and visited[r][c] == 0:
            ground = []
            q = deque()
            q.append([r, c])
            ground.append([r, c])
            visited[r][c] = 1
            while q:
                a, b = q.popleft()
                for dir in range(4):
                    na = a+dr[dir]
                    nb = b+dc[dir]
                    if 0<=na<N and 0<=nb<N and board[na][nb] == 1 and visited[na][nb] == 0:
                        q.append([na, nb])
                        ground.append([na, nb])
                        visited[na][nb] = 1
            grounds.append(ground)

result = float('inf')
for g in grounds:
    p = deque(g)
    re = []
    for x, y in p:
        board[x][y] = 2
    count = 0
    while p and count < result:
        is_ground = 0
        for _ in range(len(p)):
            c, d = p.popleft()
            for dir in range(4):
                nc = c+dr[dir]
                nd = d+dc[dir]
                if 0<=nc<N and 0<=nd<N:
                    if board[nc][nd] == 0 and visited[nc][nd] == 0:
                        p.append([nc, nd])
                        re.append([nc, nd])
                        visited[nc][nd] = 1
                    elif board[nc][nd] == 1:
                        is_ground = 1
        for i, j in re:
            visited[i][j] = 0
        if is_ground:
            if count < result:
                result = count
            break

        count += 1

print(result)
