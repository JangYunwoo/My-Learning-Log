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

parent = [i for i in range(len(grounds))] # = [0,1,2,3,2], [0,1,2,2,2]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):            #   a=2 b=4,      a=2 b=3,      a=1 b=4
    ra = find(a)            #ra=find(2)=2, ra=find(2)=2, ra=find(1)=1
    rb = find(b)            #rb=find(4)=4, rb=find(3)=3, rb=find(4)=2
    if ra != rb:
        parent[rb] = ra     #parent[4] = 2, parent[3]=2, parent[4]=1
        return True
    return False

result = 0
edge_count = 0
need = len(grounds) - 2

for cost, a, b in adj_list:     # cost=2,a=2,b=4, cost=3,a=2,b=3, cost=4,a=1,b=4
    if union(a, b):
        result += cost          # result=2, result=5,
        edge_count += 1         # edge_cost=1, edge_cost=2,
        if edge_count == need:  # need = 3
            break


if edge_count == need:
    print(result)
else:
    print(-1)