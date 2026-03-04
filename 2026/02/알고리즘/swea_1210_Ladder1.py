def move(x, y):
    if x == 0:
        result.append(y)
        return
     
    visited[x][y] = 1
    for dir in range(1, 3):
        nx = x + dr[dir]
        ny = y + dc[dir]
        if 0<=ny<=99 and not visited[nx][ny] and ladder[nx][ny]:
            move(nx, ny)
            break
    else:
        dir = 0
        move(x+dr[dir], y+dc[dir])
 
for tc in range(10):
    T = int(input())
    result = []
    visited = [[0]*100 for _ in range(100)]
 
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
 
    ladder = [list(map(int, input().split())) for _ in range(100)]
    move(99, ladder[99].index(2))
    print(f"#{T} {result[0]}")