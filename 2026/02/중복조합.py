numbers = [1,2,3,4,5]
pick_numbers = []
M = 3
pick_numbers2 = [-1] * M

# 중복 조합
def comb2(idx, count):
    if count == M:
        print(pick_numbers)
        return

    # idx : 탐색 범위 중 시작 인덱스
    # i : 고른 숫자의 인덱스
    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
        comb2(i, count+1)
        pick_numbers.pop()

comb2(0, 0)