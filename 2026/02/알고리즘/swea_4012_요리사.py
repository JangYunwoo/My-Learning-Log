from itertools import combinations

def part(count):
    global result
    
    if len(my_pick) > N//2 or len(your_pick) > N//2:
        return
    
    if count == N:
        my_score = 0
        for a, b in combinations(my_pick, 2):
            my_score += board[a][b] + board[b][a]

        your_score = 0
        for c, d in combinations(your_pick, 2):
            your_score += board[c][d] + board[d][c]

        abs_score = abs(my_score - your_score)
        if result > abs_score:
            result = abs_score
        return

    my_pick.append(count)
    part(count+1)
    my_pick.pop()
    your_pick.append(count)
    part(count+1)
    your_pick.pop()
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    foods = [i for i in range(N)]
    scores = []

    my_pick = []
    your_pick = []

    result = float('inf')
    part(0)

    print(f"#{tc} {result}")