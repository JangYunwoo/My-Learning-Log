import heapq

def solution(dist_limit, split_limit):
    visited = {}
    hq = []
    heapq.heappush(hq, [0, 1, 1])
    visited[1] = 1
    answer = 1
    while hq:
        dist, split, manswer = heapq.heappop(hq)
        if manswer > answer:
            answer = manswer
        if dist+manswer <= dist_limit:
            if split*3 <= split_limit and not visited.get(split*3):
                heapq.heappush(hq, [dist+manswer, split*3, manswer*3])
                visited[split*3] = 1
            if split*2 <= split_limit and not visited.get(split*2):
                heapq.heappush(hq, [dist+manswer, split*2, manswer*2])
                visited[split*2] = 1
        else:
            ndist = dist_limit-dist
            if ndist <= 0:
                continue
            if split*3 <= split_limit and not visited.get(split*3):
                heapq.heappush(hq, [dist+ndist, split*3, manswer+ndist*2])
                visited[split*3] = 1
            if split*2 <= split_limit and not visited.get(split*2):
                heapq.heappush(hq, [dist+ndist, split*2, manswer+ndist])
                visited[split*2] = 1
    return answer