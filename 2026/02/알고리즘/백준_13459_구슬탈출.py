def dfs(Rr, Rc, Br, Bc, dir, count):
    global result
    
    if count == 11 or result == 1:
        return
    
    R_result = 0
    for _ in range(2):
        if Rr and Rc:
            while True:
                nRr = Rr+dr[dir]
                nRc = Rc+dc[dir]
                if board[nRr][nRc] == '#' or (nRr == Br and nRc == Bc):
                    break

                elif board[nRr][nRc] == '.':
                    Rr = nRr
                    Rc = nRc

                elif board[nRr][nRc] == 'O':
                    R_result = 1
                    Rr = None
                    Rc = None
                    break
        
        while True:
            nBr = Br+dr[dir]
            nBc = Bc+dc[dir]
            if board[nBr][nBc] == '#' or (nBr == Rr and nBc == Rc):
                break
                    
            elif board[nBr][nBc] == '.':
                Br = nBr
                Bc = nBc

            elif board[nBr][nBc] == 'O':
                return
                
    if R_result == 1:
        result = 1
        return
    else:
        for ndir in range(4):
            if ndir != dir and ndir != (dir+2)%4:
                dfs(Rr, Rc, Br, Bc, ndir, count+1)
            

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for r in range(N):
    for c in range(M):
        if board[r][c] == 'R':
            Rr, Rc = r, c
            board[r][c] = '.'
        elif board[r][c] == 'B':
            Br, Bc = r, c
            board[r][c] = '.'

result = 0

for dir in range(4):
    dfs(Rr, Rc, Br, Bc, dir, 1)

print(result)