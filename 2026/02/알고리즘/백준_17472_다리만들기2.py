from collections import deque
from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[0]*M for _ in range(N)]
grounds = [[0]]
i = 1
for r in range(N):
    for c in range(M):
        if board[r][c] == 1 and visited[r][c] == 0:
            q = deque()
            q.append([r, c])
            ground = []
            ground.append([r, c])
            board[r][c] = i
            visited[r][c] = 1
            while q:
                x, y = q.popleft()
                for dir in range(4):
                    nx = x+dr[dir]
                    ny = y+dc[dir]
                    if 0<=nx<N and 0<=ny<M and board[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append([nx, ny])
                        ground.append([nx, ny])
                        board[nx][ny] = i
                        visited[nx][ny] = 1

            grounds.append(ground)
            i += 1

adj = {}
for groundnum in range(1, len(grounds)):
    adj[groundnum] = {}
    visited = [0] * len(grounds)
    visited[groundnum] = 1
    for dir in range(4):
        for a, b in grounds[groundnum]:
            j = 0
            while True:
                na = a+dr[dir]*(j+1)
                nb = b+dc[dir]*(j+1)
                if 0<=na<N and 0<=nb<M and board[na][nb] != 0 and board[na][nb] != groundnum:
                    if j > 1 and groundnum <= board[na][nb]:
                        if visited[board[na][nb]] == 0:
                            adj[groundnum][board[na][nb]] = j
                            visited[board[na][nb]] = 1
                        else:
                            if adj[groundnum][board[na][nb]] > j:
                                adj[groundnum][board[na][nb]] = j
                    else:
                        break
                    break
                elif not (0<=na<N and 0<=nb<M) or board[na][nb] == groundnum:
                    break
                j += 1

adj_list = []
for n in adj:
    for m in adj[n]:
        adj_list.append([adj[n][m], n, m])
adj_list.sort(key=lambda x: x[0])


result = float('inf')
for lines in combinations(adj_list, len(grounds)-2):
    adj2 = {}
    sum_bridge = 0
    for line in lines:
        sum_bridge += line[0]
        if adj2.get(line[1]):
            adj2[line[1]].append(line[2])
        else:
            adj2[line[1]] = [line[2]]

        if adj2.get(line[2]):
            adj2[line[2]].append(line[1])
        else:
            adj2[line[2]] = [line[1]]
        
    for k in adj2:
        adj2[k].sort()

    visited2 = [0] *len(grounds)
    q = deque()
    q.append(1)
    visited2[1] = 1
    if not adj2.get(1):
        continue
    while q:
        node = q.popleft()
        for next_node in adj2[node]:
            if visited2[next_node] == 0:
                visited2[next_node] = 1
                q.append(next_node)
    if sum(visited2) == len(grounds)-1:
        result = sum_bridge
        break

if result == float('inf'):
    print(-1)
else:
    print(result)