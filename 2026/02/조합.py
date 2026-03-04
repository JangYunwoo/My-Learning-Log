numbers = [1,2,3,4,5]
pick_numbers = []
M = 3
pick_numbers2 = [-1] * M

# 조합
def comb(idx, count):
    if count == M:
        print(pick_numbers)
        return

    # idx : 탐색 범위 중 시작 인덱스
    # i : 고른 숫자의 인덱스
    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
        comb(i+1, count+1)
        pick_numbers.pop()

comb(0, 0)

#(0,0)
# i가 0~4여서 1,2,3,4,5를 뽑을거임
# 두번째에서는 i가 1~4임. 즉 2,3,4,5를 뽑을거임
# 세번째는 i가 2~4, 즉 3,4,5를 추출 - 1,2,(3,4,5)
# 두번째 숫자가 3임. 세번째에서 4,5를 뽑음1,3,(4,5) 