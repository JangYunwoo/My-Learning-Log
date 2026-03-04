N = int(input())
 
for i in range(1, N + 1):
    A = list(map(int, input().split()))
    print(f"#{i} {int(sum(A)/10 + 0.5)}")