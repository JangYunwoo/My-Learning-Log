dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
d = {
    '^': 0,
    '>': 1,
    'v': 2,
    '<': 3,
    0: '^',
    1: '>',
    2: 'v',
    3: '<'
}

T = int(input())

for tc in range(1,T+1):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]

    for r in range(H):
        for c in range(W):
            if d.get(board[r][c]) is not None:
                dir = d[board[r][c]]
                board[r][c] = '.'
                x = r
                y = c

    N = int(input())
    orders = input()
    for order in orders:
        if order == 'U':
            dir = 0
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<H and 0<=ny<W and board[nx][ny] == '.':
                x = nx
                y = ny
        
        elif order == 'R':
            dir = 1
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<H and 0<=ny<W and board[nx][ny] == '.':
                x = nx
                y = ny

        elif order == 'D':
            dir = 2
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<H and 0<=ny<W and board[nx][ny] == '.':
                x = nx
                y = ny

        elif order == 'L':
            dir = 3
            nx = x+dr[dir]
            ny = y+dc[dir]
            if 0<=nx<H and 0<=ny<W and board[nx][ny] == '.':
                x = nx
                y = ny

        elif order == 'S':
            i = 1
            while True:
                nx = x+dr[dir]*i
                ny = y+dc[dir]*i
                if 0<=nx<H and 0<=ny<W:
                    if board[nx][ny] == '*':
                        board[nx][ny] = '.'
                        break
                    elif board[nx][ny] == '#':
                        break
                else:
                    break
                i += 1
    board[x][y] = d[dir]
    print(f"#{tc}", end=' ')
    for row in range(H):
        print(''.join(board[row]))
