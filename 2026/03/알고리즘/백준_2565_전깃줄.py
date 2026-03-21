import bisect

N = int(input())

tower = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

endtower = [tower[i][1] for i in range(N)]

lsi = [endtower[0]]
for i in range(1,N):
    if endtower[i] > lsi[-1]:
        lsi.append(endtower[i])
    else:
        idx = bisect.bisect(lsi, endtower[i])
        lsi[idx] = endtower[i]

print(N-len(lsi))