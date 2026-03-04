import sys
input = sys.stdin.readline

def search(r, c, num):
    global result
    if r == N:
        if result < num:
            result = num
        return

    if c == N-1:
        nr = r+1
        nc = 0
    else:
        nr = r
        nc = c+1
    if board[r][c] == 0:
        search(nr, nc, num)
        return
    elif not plus[r+c] and not sub[r-c+N-1]:
        plus[r+c] = 1
        sub[r-c+N-1] = 1
        search(nr, nc, num+1)
        plus[r+c] = 0
        sub[r-c+N-1] = 0
    search(nr, nc, num)
    return
    
            
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
    
plus = [0]*(2*N-1)
sub = [0]*(2*N-1)

result = 0

search(0, 0, 0)

print(result)