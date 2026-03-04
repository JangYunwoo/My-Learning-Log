T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    board = [list(map(int, input().split())) for _ in range(N)]
    change_board = list(zip(*board))
    for b in [board, change_board]:
        for r in range(N):
            count = 0
            for c in range(N):
                if b[r][c] == 0:
                    if count == K:
                        result += 1
                    count = 0
                else:
                    count += 1
            if count == K:
                result += 1

    print(f"#{tc} {result}")