def search(node):
    visited[node] = 1
    if route.get(node):
        for i in route[node]:
            if visited[i] == 0:
                search(i)
    else:
        return
    
    return

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    visited = [0]*(V+1)
    route = {}
    for _ in range(E):
        A, B = map(int, input().split())
        if route.get(A):
            route[A] += [B]
        else:
            route[A] = [B]

    S, G = map(int, input().split())

    search(S)
    if visited[G] == 1:
        result = 1
    else:
        result = 0

    print(f"#{tc} {result}")