N, M = map(int, input().split())
board = [input() for _ in range(N)]
color = {
    0: 'B',
    1: 'W'
}

result = float('inf')
for i in range(N-7):
    for j in range(M-7):
        test_board = [board[m][j:j+8] for m in range(i,i+8)]
        count = 0

        same = 0
        for r in range(8):
            for c in range(8):
                if test_board[r][c] != color[same]:
                    count += 1
                same = (same+1)%2
            same = (same+1)%2
        
        if result > count:
            result = count

        count = 0

        same = 1
        for r in range(8):
            for c in range(8):
                if test_board[r][c] != color[same]:
                    count += 1
                same = (same+1)%2
            same = (same+1)%2
        
        if result > count:
            result = count

print(result)