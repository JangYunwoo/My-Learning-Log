from pprint import pprint

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

T = int(input())

for tc in range(1,T+1):
    M, A = map(int, input().split())
    A_root = [0] + list(map(int, input().split()))
    B_root = [0] + list(map(int, input().split()))

    board = [[0]*11 for _ in range(11)]
    BC_P = {}
    for BC_num in range(A):
        BC_c, BC_r, C, P = map(int, input().split())
        BC_P[BC_num] = P

        for i in range(-C, C+1):
            for j in range(abs(i)-C, abs(abs(i)-C)+1):
                if 1<=BC_r+i<11 and 1<=BC_c+j<11:
                    if board[BC_r+i][BC_c+j] == 0:
                        board[BC_r+i][BC_c+j] = [BC_num]
                    else:
                        board[BC_r+i][BC_c+j].append(BC_num)
    for r in range(11):
        for c in range(11):
            if board[r][c] != 0 and len(board[r][c])>1:
                board[r][c].sort(key=lambda x: BC_P[x])
    
    A_x = 1
    A_y = 1
    B_x = 10
    B_y = 10
    result = 0
    for sec in range(M+1):
        A_x += dr[A_root[sec]]
        A_y += dc[A_root[sec]]
        B_x += dr[B_root[sec]]
        B_y += dc[B_root[sec]]
        
        if board[A_x][A_y] != 0 and board[B_x][B_y] != 0 and board[A_x][A_y][-1] == board[B_x][B_y][-1]:
            if len(board[A_x][A_y]) == 1 and len(board[B_x][B_y]) == 1:
                result += BC_P[board[A_x][A_y][-1]]
            else:
                result += sum([BC_P[k] for k in sorted(list(set(board[A_x][A_y]+board[B_x][B_y])), key=lambda x: BC_P[x])[-2:]])
            continue
        
        if board[A_x][A_y] != 0:
            result += BC_P[board[A_x][A_y][-1]]
        if board[B_x][B_y] != 0:
            result += BC_P[board[B_x][B_y][-1]]
    print(f"#{tc} {result}")