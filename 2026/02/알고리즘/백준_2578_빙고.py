my_bingo = {}
my_board = []

for r in range(5):
    c_bingo = list(map(int, input().split()))
    my_board.append(c_bingo)

    for c in range(5):
        my_bingo[c_bingo[c]] = [r, c]

count = 0
for r in range(5):
    your_bingo = list(map(int, input().split()))

    for c in your_bingo:
        x, y = my_bingo[c]
        my_board[x][y] = 0
        count += 1
        
        bingo = 0
        sub_board = list(zip(*my_board))
        for i in range(5):
            if sum(my_board[i]) == 0:
                bingo += 1
            if sum(sub_board[i]) == 0:
                bingo += 1
        if sum([my_board[0][0], my_board[1][1], my_board[2][2], my_board[3][3], my_board[4][4]]) == 0:
            bingo += 1
        if sum([my_board[0][4], my_board[1][3], my_board[2][2], my_board[3][1], my_board[4][0]]) == 0:
            bingo += 1
        if bingo >= 3:
            print(count)
            exit()