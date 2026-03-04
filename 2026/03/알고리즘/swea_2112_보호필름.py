import copy

def search(count, drug_count):
    global result
    if drug_count >= result:
        return
    if count == D:
        nfilm = copy.deepcopy(film)
        for floor in range(D):
            if select[floor] == 1:
                nfilm[floor] = A
            elif select[floor] == 2:
                nfilm[floor] = B

        test = list(zip(*nfilm))
        test_pass = 0
        for line in range(W):
            test_d = 1
            for num in range(1, D):
                if test[line][num] == test[line][num-1]:
                    test_d += 1
                    if test_d == K:
                        test_pass += 1
                        break
                else:
                    test_d = 1
            if line+1 != test_pass:
                break
        if test_pass == W:
            if drug_count <= result:
                result = drug_count
                
        return

    for i in [0, 1, 2]:
        select.append(i)
        search(count+1, drug_count if i == 0 else drug_count+1)
        select.pop()
    return


T = int(input())

for tc in range(1,T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    select = []
    result = K
    A = [0]*W
    B = [1]*W
    search(0, 0)

    print(f"#{tc} {result}")