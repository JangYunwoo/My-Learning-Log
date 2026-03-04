T = int(input())
 
for i in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    sum_lst = []
 
    for j in range(N - M + 1):
        sum_lst.append(sum(a[j:j+M]))
 
    result = max(sum_lst) - min(sum_lst)
 
    print(f"#{i+1} {result}")