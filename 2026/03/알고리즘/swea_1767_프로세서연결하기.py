def dfs(count, success, linesum):
    global succ, result
    if success > succ:
        succ = success
        result = linesum
    elif success == succ:
        if linesum < result:
            result = linesum
    if count == corenum:
        return
    for dir in range(4):
        x, y = corexy[count]
        linecount = 0
        switch = 0
        if dir == 0:
            for i in range(x-1, -1, -1):
                if visited[i][y] == 0:
                    visited[i][y] = 2
                    linecount += 1
                else:
                    switch = 1
                    for i in range(x-1, x-linecount-1, -1):
                        visited[i][y] = 0
                    break
            if switch == 1:
                continue
            dfs(count+1, success+1, linesum+linecount)
            for i in range(x):
                if visited[i][y] != 1:
                    visited[i][y] = 0
        if dir == 1:
            for i in range(x+1, N):
                if visited[i][y] == 0:
                    visited[i][y] = 2
                    linecount += 1
                else:
                    switch = 1
                    for i in range(x+1, x+linecount+1):
                        visited[i][y] = 0
                    break
            if switch == 1:
                continue
            dfs(count+1, success+1, linesum+linecount)
            for i in range(x+1, N):
                if visited[i][y] != 1:
                    visited[i][y] = 0
        if dir == 2:
            for i in range(y-1, -1, -1):
                if visited[x][i] == 0:
                    visited[x][i] = 2
                    linecount += 1
                else:
                    switch = 1
                    for i in range(y-1, y-linecount-1, -1):
                        visited[x][i] = 0
                    break
            if switch == 1:
                continue
            dfs(count+1, success+1, linesum+linecount)
            for i in range(y):
                if visited[x][i] != 1:
                    visited[x][i] = 0
        if dir == 3:
            for i in range(y+1, N):
                if visited[x][i] == 0:
                    visited[x][i] = 2
                    linecount += 1
                else:
                    switch = 1
                    for i in range(y+1, y+linecount+1):
                        visited[x][i] = 0
                    break
            if switch == 1:
                continue
            dfs(count+1, success+1, linesum+linecount)
            for i in range(y+1, N):
                if visited[x][i] != 1:
                    visited[x][i] = 0
    dfs(count+1, success, linesum)
    return
 
T = int(input())
 
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
 
    corenum = 0
    corexy = []
    pickdir =[]
    visited = [[0]*N for _ in range(N)]
    cornercore = 0
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                if r != 0 and r != N-1 and c != 0 and c != N-1:
                    corenum += 1
                    corexy.append([r, c])
                else:
                    cornercore += 1
                visited[r][c] = 1
     
    succ = 0
    result = 0
    dfs(0, 0, 0)
 
    print(f"#{tc} {result}")