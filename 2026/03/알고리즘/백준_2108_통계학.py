N = int(input())
num = []
numpop = {}

for _ in range(N):
    anum = int(input())
    num.append(anum)
    if numpop.get(anum):
        numpop[anum] += 1
    else:
        numpop[anum] = 1

num.sort()
finalnumpop = sorted(list(set(num)), key=lambda x: (-numpop[x], x))
sumnum = sum(num)

if sumnum >= 0:
    print(int(sumnum/N + 0.5))
else:
    print(-int(-sumnum/N + 0.5))
print(num[N//2])
if len(finalnumpop) > 1 and numpop[finalnumpop[0]] == numpop[finalnumpop[1]]:
    print(finalnumpop[1])
else:
    print(finalnumpop[0])
print(num[-1]-num[0])