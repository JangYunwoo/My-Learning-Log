'''
def perm(count):
    global result
    if count == 9:
        a_score = go_score()
        if result < a_score:
            result = a_score
        return
    
    if count == 3:
        order.append(0)
        perm(count+1)
        order.pop()
    else:
        for i in range(1,9):
            if visited[i] == 0:
                order.append(i)
                visited[i] = 1
                perm(count+1)
                order.pop()
                visited[i] = 0

    return

def go_score():
    score = 0
    i = 0
    for bat in total_bat:
        base=[0, 0, 0, 0]

        out = 0
        while out < 3:
            if bat[order[i]] == 0:
                out += 1
            elif bat[order[i]] == 1:
                score += base[3]
                base[3] = 0
                for j in range(2, 0, -1):
                    if base[j] == 1:
                        base[j+1] = 1
                        base[j] = 0
                base[1] = 1
            elif bat[order[i]] == 2:
                score += base[3] + base[2]
                base[3], base[2] = 0, 0
                if base[1] == 1:
                    base[3] = 1
                    base[1] = 0
                base[2] = 1
            elif bat[order[i]] == 3:
                score += base[3] + base[2] + base[1]
                base[3], base[2], base[1] = 0, 0, 0
                base[3] = 1
            else:
                score += base[3] + base[2] + base[1] + 1
                base[3], base[2], base[1] = 0, 0, 0
            i = (i+1)%9

    return score

N = int(input())

total_bat = [list(map(int, input().split())) for _ in range(N)]
visited = [0]*9
order = []
result = float('-inf')

perm(0)
print(result)
'''

def perm(count):
    global result

    if count == 9:
        a_score = go_score()
        if result < a_score:
            result = a_score
        return

    if count == 3:
        order.append(0)
        perm(count + 1)
        order.pop()
    else:
        for i in range(1, 9):
            if visited[i] == 0:
                order.append(i)
                visited[i] = 1
                perm(count + 1)
                order.pop()
                visited[i] = 0

    return


def go_score():
    score = 0
    i = 0

    for bat in total_bat:
        base = [0, 0, 0, 0]
        out = 0

        while out < 3:
            base[0] = 1

            if bat[order[i]] == 0:
                out += 1

            elif bat[order[i]] == 1:
                score += base[3]
                base[3] = 0
                for j in range(2, -1, -1):
                    base[j + 1], base[j] = base[j], base[j + 1]

            elif bat[order[i]] == 2:
                score += base[3] + base[2]
                base[3], base[2] = 0, 0
                for j in range(1, -1, -1):
                    base[j + 2], base[j] = base[j], base[j + 2]

            elif bat[order[i]] == 3:
                score += base[3] + base[2] + base[1]
                base[3], base[2], base[1] = 0, 0, 0
                for j in range(1):
                    base[j + 3], base[j] = base[j], base[j + 3]

            else:
                score += base[3] + base[2] + base[1] + base[0]
                base[3], base[2], base[1] = 0, 0, 0

            i = (i + 1) % 9

    return score


N = int(input())
total_bat = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * 9
order = []
result = float('-inf')

perm(0)
print(result)