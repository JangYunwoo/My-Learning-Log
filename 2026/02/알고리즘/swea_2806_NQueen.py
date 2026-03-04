def search(r, num):
    if num == N+1:
        global result
        result += 1
        return

    for c in range(N):
        if not plus[r+c] and not sub[r-c+N-1] and not col[c]:
            plus[r+c] = 1
            sub[r-c+N-1] = 1
            col[c] = 1
            search(r+1, num+1)
            plus[r+c] = 0
            sub[r-c+N-1] = 0
            col[c] = 0
            
N = int(input())
    
plus = [0]*(2*N-1)
sub = [0]*(2*N-1)
col = [0]*N

result = 0

search(0, 1)

print(result)