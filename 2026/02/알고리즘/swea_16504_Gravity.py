T = int(input())
 
for p in range(T):
    N = int(input())
    box = list(map(int, input().split()))
 
    result = 0
 
    for i in range(N):
        drop = N - i - 1
        for j in box[i + 1:]:
            if box[i] <= j:
                drop -= 1
        if result < drop:
            result = drop
 
    print(f"#{p+1} {result}")