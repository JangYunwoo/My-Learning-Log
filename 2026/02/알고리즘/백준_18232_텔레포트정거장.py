from collections import deque

N, M = map(int, input().split())
S, E = map(int, input().split())

visited = [0]*(N+1)
relation = {}
q = deque()

for i in range(1, N+1):
    relation[i] = []

for i in range(1, N):
    relation[i].append(i+1)
    relation[i+1].append(i)

for _ in range(M):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

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