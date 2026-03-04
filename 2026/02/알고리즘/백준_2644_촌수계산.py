from collections import deque

n = int(input())
S, E = map(int, input().split())
N = int(input())

visited = [0]*(n+1)
relation = {}
q = deque()

for _ in range(N):
    a, b = map(int, input().split())
    if relation.get(a):
        relation[a].append(b)
    else:
        relation[a] = [b]

    if relation.get(b):
        relation[b].append(a)
    else:
        relation[b] = [a]

for i in relation:
    relation[i].sort()

count = 0
q.append(S)

while q:
    count += 1
    for _ in range(len(q)):
        person = q.popleft()
        for other_person in relation[person]:
            if visited[other_person] == 0:
                q.append(other_person)
                visited[other_person] = 1
    
    if visited[E] == 1:
        print(count)
        break
else:
    print(-1)