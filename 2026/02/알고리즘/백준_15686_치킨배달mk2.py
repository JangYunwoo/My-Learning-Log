def comb(idx, count):
    if count == M:
        new_pick_chick = pick_chick.copy()
        length_list = []
        for i in house:
            length = []
            for j in new_pick_chick:
                length.append(abs(i[0]-j[0]) + abs(i[1]-j[1]))
            length_list.append(min(length))
        chick_length_list.append(sum(length_list))
        return

    for i in range(idx, len(chick)):
        pick_chick.append(chick[i])
        comb(i+1, count+1)
        pick_chick.pop()
    
    return

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chick = []
pick_chick = []

house = []
chick_length_list = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            chick.append([r, c])
        elif city[r][c] == 1:
            house.append([r, c])

comb(0,0)
print(min(chick_length_list))