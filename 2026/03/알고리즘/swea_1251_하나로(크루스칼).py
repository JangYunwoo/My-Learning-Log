def find(c_node):
    if parent[c_node] != c_node:
        parent[c_node] = find(parent[c_node])
    return parent[c_node]

def union(node_1, node_2):
    node_1 = find(node_1)
    node_2 = find(node_2)
    if node_1 != node_2:
        parent[node_2] = node_1
        return True
    return False

T = int(input())

for C in range(1,T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    island = []
    for i in range(N-1):
        for j in range(i+1, N):
            island.append([abs(X[i]-X[j])**2+abs(Y[i]-Y[j])**2, i, j])
    
    island.sort(key=lambda x: x[0])
    parent = [l for l in range(N)]
    build = 0
    result = 0

    for L, S, G in island:
        if union(S, G):
            result += E*L
            build += 1
            if build == N-1:
                break

    print(f"#{C} {int(result+0.5)}")
