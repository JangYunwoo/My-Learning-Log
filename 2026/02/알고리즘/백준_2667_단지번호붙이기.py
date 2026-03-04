dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = int(input())

area = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]

def search(x, y):
    visited[x][y] = 1
    global count_house
    count_house += 1
    for dir in range(4):
        if (0 <= (x + dr[dir]) < N and 0 <= (y + dc[dir]) < N and
            visited[x+dr[dir]][y+dc[dir]] == 0 and area[x+dr[dir]][y+dc[dir]] == 1):
            search(x+dr[dir], y+dc[dir])
    else:
        return

area_num = []
count = 0
count_house = 0

for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            if visited[i][j]:
                continue
            else:
                count += 1
                search(i, j)
                area_num.append(count_house)
                count_house = 0

print(count)
area_num.sort()
for i in area_num:
    print(i)