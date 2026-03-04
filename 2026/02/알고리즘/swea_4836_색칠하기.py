T = int(input())
 
for tc in range(T):
 
    tile = [[0]*10 for _ in range(10)]
    result = 0
 
    N = int(input())
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
 
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                tile[i][j] += color
                if tile[i][j] == 3:
                    result += 1
                     
    print(f"#{tc+1} {result}")