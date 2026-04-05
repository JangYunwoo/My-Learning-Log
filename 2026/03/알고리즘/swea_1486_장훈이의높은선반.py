def comb(idx, count, sm):
    global result
    if sm >= B:
        if result > sm:
            result = sm
        return
    if count == N:
        return
    
    for i in range(idx, N):
        comb(i+1,count+1,sm+heights[i])
    return


T = int(input())

for tc in range(1,T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    pick = []
    result = float('inf')
    comb(0, 0, 0)
    print(f"#{tc} {result - B}")