def search(node):
    visited[node] = 1
    if route.get(node):
        for i in route[node]:
            if visited[i] == 0:
                search(i)
    else:
        return
    
    return

for _ in range(10):
    tc, N = map(int, input().split())
    route_list = list(map(int, input().split()))
    visited = [0]*100
    route = {}
    for i in range(N):
        if route.get(route_list[2*i]):
            route[route_list[2*i]] += [route_list[2*i+1]]
        else:
            route[route_list[2*i]] = [route_list[2*i+1]]

    search(0)
    if visited[99] == 1:
        result = 1
    else:
        result = 0

    print(f"#{tc} {result}")