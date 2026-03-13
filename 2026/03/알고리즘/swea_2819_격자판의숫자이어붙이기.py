def dfs(x, y, count):
    if count == 7:
        result.add(tuple(pick_nums))
        return
    
    for dir in range(4):
        nx = x+dr[dir]
        ny = y+dc[dir]
        if 0<=nx<4 and 0<=ny<4:
            pick_nums.append(board[nx][ny])
            dfs(nx, ny, count+1)
            pick_nums.pop()
    return


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())

for tc in range(1,T+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    nums = [0]*10
    pick_nums = []
    result = set()
    for r in range(4):
        for c in range(4):
            pick_nums.append(board[r][c])
            dfs(r, c, 1)
            pick_nums.pop()
    
    print(f"#{tc} {len(result)}")