import heapq
import sys
input = sys.stdin.readline

def search(graph, start):
    length[start] = 0
    hq = [(0, start)]

    while hq:
        ccost, cnode = heapq.heappop(hq)
        if ccost > length[cnode]:
            continue
        
        if graph.get(cnode):
            for nnode, cost in graph[cnode].items():
                ncost = ccost + cost

                if ncost < length[nnode]:
                    length[nnode] = ncost
                    heapq.heappush(hq, (ncost, nnode))

N, M, K = map(int, input().split())

road = {}
for i in range(M):
    U, V, C = map(int, input().split())
    if road.get(V):
        road[V][U] = C
    else:
        road[V] = {U: C}
interview = list(map(int, input().split()))

length = [0]+[float('inf')]*N

for j in interview:
    search(road, j)

result_node = 0
result = 0
for n in range(1, N+1):
    if length[n] > result:
        result_node = n
        result = length[n]
print(result_node)
print(result)