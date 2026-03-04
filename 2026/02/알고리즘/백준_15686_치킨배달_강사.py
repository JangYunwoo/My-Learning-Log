from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

chicken_rcs = []
home_rcs = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            chicken_rcs.append((i, j))
        elif graph[i][j] == 1:
            home_rcs.append((i, j))

distances = [[0]*len(chicken_rcs) for _ in range(len(home_rcs))]
for i in range(len(home_rcs)):
    for j in range(len(chicken_rcs)):
        distances[i][j] = abs(home_rcs[i][0] - chicken_rcs[j][0]) + abs(home_rcs[i][1] - chicken_rcs[j][1])

answer = float('inf')
for comb_case in combinations(range(len(chicken_rcs)), M):
    comb_case_dis = 0
    for i in range(len(home_rcs)):
        dis = float('inf')
        for j in comb_case:
            if dis > distances[i][j]:
                dis = distances[i][j]
        comb_case_dis += dis
    
    if answer > comb_case_dis:
        answer = comb_case_dis

print(answer)

# 1 2 3 4 5

# A 

# B