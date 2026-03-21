import bisect

N = int(input())

tower = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
count = [0]
lsi = [tower[0][0]]
for i in range(1,N):
    if tower[i][0] > lsi[-1]:
        count.append(len(lsi))
        lsi.append(tower[i][0])

    else:
        idx = bisect.bisect(lsi, tower[i][0])
        lsi[idx] = tower[i][0]
        count.append(idx)
print(N-len(lsi))
result = []
i = len(lsi)-1
while i >= 0:
    for j in range(len(count)-1,-1,-1):
        if i == count[j]:
            i -= 1
        else:
            result.append(tower[j][0])
for k in result:
    print(k)