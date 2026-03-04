def test(lst):
    test_result = 1
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            test_result = 0
 
    return test_result
 
for tc in range(1,11):
    relen = int(input())
    word_board = [list(input()) for _ in range(8)]
    ch_board = list(zip(*word_board))
 
    result = 0
    for board in [word_board, ch_board]:
        for i in range(8):
            for j in range(8-relen+1):
                if test(board[i][j:j+relen]):
                    result += 1
 
    print(f"#{tc} {result}")