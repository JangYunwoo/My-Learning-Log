def search(count, drug_count):
    global result
    if drug_count >= result:
        return
    if count == D:
        test_pass = 0
        for line in range(W):
            test_d = 1
            for num in range(1, D):
                if film[num][line] == film[num-1][line]:
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
    backup = film[count]
    
    search(count+1, drug_count)
    film[count] = A
    search(count+1, drug_count+1)
    film[count] = backup
    film[count] = B
    search(count+1, drug_count+1)
    film[count] = backup
    return
T = int(input())

for tc in range(1,T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    
    if K==1:
        print(f"#{tc} 0")
        continue
    result = K
    A = [0]*W
    B = [1]*W
    search(0, 0)

    print(f"#{tc} {result}")