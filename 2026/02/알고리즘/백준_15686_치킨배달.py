from collections import deque

def comb(idx, count):
    if count == M:
        q.append(pick_chick[0])
        search(city.copy())
        return
    
    for i in range(idx, len(chick)):
        pick_chick[0].append(chick[i])
        comb(idx+1, count+1)
        pick_chick[0].pop()
    
    return

def search(arr):
    i = 1
    length = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dir in range(4):
                nx = x + dr[dir]
                ny = y + dr[dir]
                if 0<=nx<N and 0<=ny<N and arr[nx][ny] == 0:
                    arr[nx][ny] = 3
                    q.append([nx, ny])
                elif 0<=nx<N and 0<=ny<N and arr[nx][ny] == 1:
                    house -= 1
                    length += i
                    arr[nx][ny] = 3
        if house == 0:
            chick_length.append(length)
            break
        i += 1
    return

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
house = 0
chick = deque()
chick_length = deque()
pick_chick = deque([[]])
q = deque()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house += 1
        elif city[r][c] == 2:
            chick.append([r, c])
            city[r][c] = 3

comb(0, 0)
print(min(chick_length))