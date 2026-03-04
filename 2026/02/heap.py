import heapq

def dijkstra(graph, start):
    # distances는 시작 노드에서 각 노드까지의 최단 거리를 저장하는 딕셔너리입니다.
    distances = {node: float('inf') for node in graph}
    # 시작 노드에서 자기 자신으로 가는 거리는 0으로 설정합니다.
    distances[start] = 0
    # 우선순위 큐를 생성합니다. 시작 노드부터 처리하므로 (0, start)를 추가합니다.
    priority_queue = [(0, start)]

    while priority_queue:
        # 현재 가장 가까운 노드를 우선순위 큐에서 꺼냅니다.
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드라면 무시합니다.
        if current_distance > distances[current_node]:
            continue

        # 현재 노드의 모든 이웃 노드를 확인합니다.
        for neighbor, weight in graph[current_node].items():
            # 현재 노드를 거쳐서 이웃 노드로 가는 거리입니다.
            distance = current_distance + weight

            # 이 거리(distance)가 기존에 저장된 거리보다 짧다면, 업데이트합니다.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 이웃 노드를 우선순위 큐에 추가합니다.
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 예시 그래프
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'E': 2, 'D': 6},
    'C': {'A': 2, 'E': 3, 'F': 8},
    'D': {'B': 6, 'E': 1},
    'E': {'B': 2, 'C': 3, 'D': 1, 'F': 7},
    'F': {'C': 8, 'E': 7}
}

print(dijkstra(graph, 'B')['D']) #{'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 3, 'F': 10}