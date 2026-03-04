T = int(input())
 
for tc in range(T):
 
    N = int(input())
    snail = [[0 for _ in range(N)] for _ in range(N)]
 
    x, y = 0, 0
    count = 1
    dest = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
 
    while count <= N**2:
        snail[x][y] = count
        count += 1
        if (not 0 <= (x + dr[dest]) < N or not 0 <= (y + dc[dest]) < N) or snail[x + dr[dest]][y + dc[dest]]:
            dest = (dest + 1) % 4
        x += dr[dest]
        y += dc[dest]
 
    print(f"#{tc+1}")
    for i in snail:
        for j in i:
            print(j, end=" ")
        print()