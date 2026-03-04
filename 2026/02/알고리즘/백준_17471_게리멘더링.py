from collections import deque

def pick_npick(count):
    if count == N+1:
        search()
        return
    
    pick.append(count)
    pick_npick(count+1)
    pick.pop()
    npick.append(count)
    pick_npick(count+1)
    npick.pop()

    return

def search():
    global result
    if abs(len(pick) - len(npick)) == N:
        return

    q = deque()
    for i in npick:
        visited[i] = 1
    q.append(pick[0])
    p_count = 1
    visited[pick[0]] = 1
    while q:
        p_node = q.popleft()
        for j in adj[p_node]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1
                p_count += 1
    
    for i in range(N+1):
        visited[i] = 1
    if len(pick) != p_count:
        return
    
    q = deque()
    for i in pick:
        visited[i] = 1
    q.append(npick[0])
    np_count = 1
    visited[npick[0]] = 1
    while q:
        np_node = q.popleft()
        for j in adj[np_node]:
            if visited[j] == 0:
                q.append(j)
                visited[j] = 1
                np_count += 1
    
    for i in range(N+1):
        visited[i] = 0
    if len(npick) != np_count:
        return
    
    p_sum = 0
    np_sum = 0
    for i in pick:
        p_sum += population[i]
    for i in npick:
        np_sum += population[i]
    
    sub = abs(p_sum - np_sum)
    if sub < result:
        result = sub


N = int(input())
adj = {}
pick = []
npick = []
visited = [0]*(N+1)
population = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    nodes = list(map(int, input().split()))
    adj[i] = sorted(nodes[1:])

result = float('inf')

pick_npick(1)
if result == float('inf'):
    result = -1
    
print(result)