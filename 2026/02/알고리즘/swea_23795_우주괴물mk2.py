from collections import deque

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    monster = []
    result = 0

    for r in range(N):
        for c in range(N):
            if board[r][c] == 2:
                monster = [r, c]
            elif board[r][c] == 0:
                result += 1

    x, y = monster
    if_count = 0
    count = 0

    for i in range(N):
        if not board[i][y]:
            count += 1
        elif board[i][y] == 1:
            if if_count:
                result -= count
                if_count = 0
            count = 0
        else:
            if_count = 1

    if if_count:
        result -= count

    if_count = 0
    count = 0

    for i in range(N):
        if not board[x][i]:
            count += 1
        elif board[x][i] == 1:
            if if_count:
                result -= count
                if_count = 0
            count = 0
        else:
            if_count = 1
            
    if if_count:
        result -= count
    
    print(f"#{tc} {result}")
        
    