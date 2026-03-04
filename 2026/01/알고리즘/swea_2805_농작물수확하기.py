T = int(input())
 
for k in range(T):
    N = int(input())
    farm = [input() for _ in range(N)]
 
    score = 0
 
    for i in range(N):
        for j in farm[i][abs(N // 2 - i):N - abs(N // 2 - i)]:
            score += int(j)
 
    print(f"#{k + 1} {score}")