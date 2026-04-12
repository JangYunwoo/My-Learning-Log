def solution(n, infection, edges, k):
    def search(count, pipe, ifcount, lst):
        nonlocal result
        nlst = []
        nifcount = ifcount
        for node in lst:
            if adj[pipe].get(node):
                for next_node in adj[pipe][node]:
                    if visited[next_node] == 0:
                        nlst.append(next_node)
                        visited[next_node] = 1
                        nifcount += 1

        for _ in range(n):
            switch = 0
            for node in nlst:
                if adj[pipe].get(node):
                    for next_node in adj[pipe][node]:
                        if visited[next_node] == 0:
                            nlst.append(next_node)
                            visited[next_node] = 1
                            nifcount += 1
                            switch = 1
            if switch == 0:
                break
        
        if count+1 == k:
            for rollbacknode in nlst:
                visited[rollbacknode] = 0
            if result < nifcount:
                result = nifcount
        else:
            for npipe in range(1,4):
                search(count+1, npipe, nifcount, lst + nlst)
            for rollbacknode in nlst:
                visited[rollbacknode] = 0
        return
        
    adj = {
        1: {},
        2: {},
        3: {}
    }

    for s, e, w in edges:
        if adj[w].get(s):
            adj[w][s].append(e)
        else:
            adj[w][s] = [e]

    for s, e, w in edges:
        if adj[w].get(e):
            adj[w][e].append(s)
        else:
            adj[w][e] = [s]
    
    lst = []
    lst.append(infection)
    result = float('-inf')
    visited = [0]*(n+1)
    visited[infection] = 1
    for pipe in range(1,4):
        search(0, pipe, 1, lst)
    
    return result