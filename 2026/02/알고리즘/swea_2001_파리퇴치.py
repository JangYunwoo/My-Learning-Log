T = int(input())
 
for tc in range(T):
     
    score = []
 
    N, M = map(int, input().split())
    fly= [list(map(int, input().split())) for _ in range(N)]
 
    for r in range(N - M + 1):
        for c in range(N - M + 1):
            score.append(sum([sum(fly[i][c:c+M]) for i in range(r, r+M)]))
 
    print(f"#{tc+1} {max(score)}")