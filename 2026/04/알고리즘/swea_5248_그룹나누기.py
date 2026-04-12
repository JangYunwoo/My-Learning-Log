def union(x, y):
    rootx = find(x)
    rooty = find(y)
 
    if rootx != rooty:        
        parent[rooty] = rootx
        return 1
    return 0
 
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
 
T = int(input())
 
for tc in range(1,T+1):
    N, M = map(int, input().split())
    result = N
 
    parent = [i for i in range(N+1)]
    want_team = iter(map(int, input().split()))
    for _ in range(M):
        a = next(want_team)
        b = next(want_team)
        result -= union(a, b)
 
    print(f"#{tc} {result}")