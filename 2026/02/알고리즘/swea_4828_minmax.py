T = int(input())
 
for i in range(T):
    N = int(input())
 
    a = list(map(int, input().split()))
 
    print(f"#{i+1} {max(a)-min(a)}")