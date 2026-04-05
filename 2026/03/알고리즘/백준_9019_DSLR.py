from collections import deque

def D(num):
    return (num*2)%10000

def S(num):
    return (num-1)%10000

def L(num):
    num_str = str(num).zfill(4)
    result = num_str[1:] + num_str[0]
    return int(result)

def R(num):
    num_str = str(num).zfill(4)
    result = num_str[-1] + num_str[:-1]
    return int(result)

N = int(input())

for _ in range(N):
    start, end = map(int, input().split())
    q = deque()
    order = ''
    q.append([start, order])
    visited = [0]*(10000)
    visited[start] = 1
    while True:
        current, corder = q.popleft()
        if current == end:
            print(corder)
            break
        test = D(current)
        if visited[test] == 0:
            q.append([test, corder + 'D'])
            visited[test] = 1
        test = S(current)
        if visited[test] == 0:
            q.append([test, corder + 'S'])
            visited[test] = 1
        test = L(current)
        if visited[test] == 0:
            q.append([test, corder + 'L'])
            visited[test] = 1
        test = R(current)
        if visited[test] == 0:
            q.append([test, corder + 'R'])
            visited[test] = 1