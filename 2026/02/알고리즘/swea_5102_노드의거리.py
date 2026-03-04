from collections import deque

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

        if route.get(B):
            route[B] += [A]
        else:
            route[B] = [A]

    for i in route:
        route[i].sort()

    S, G = map(int, input().split())
    q = deque()
    q.append(S)
    visited[S] = 1
    result = 0
    while q:
        result += 1
        for _ in range(len(q)):
            a = q.popleft()
            for i in route[a]:
                if visited[i] == 0:
                    q.append(i)
                    visited[i] = 1

        if visited[G] == 1:
            break
    else:
        result = 0
    

    print(f"#{tc} {result}")