def dfs(x, y, count, num):
    if count == 7:
        result.add(num)
        return
    
    for dir in range(4):
        nx = x+dr[dir]
        ny = y+dc[dir]
        if 0<=nx<4 and 0<=ny<4:
            dfs(nx, ny, count+1, num*10 + board[nx][ny])
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1,T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    for r in range(4):
        for c in range(4):
            dfs(r, c, 1, 10+board[r][c])
    
    print(f"#{tc} {len(result)}")