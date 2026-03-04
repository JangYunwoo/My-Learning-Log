for i in range(10):
    dn = int(input())
    box = list(map(int, input().split()))
 
    for _ in range(dn):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
 
    print(f"#{i+1} {max(box)-min(box)}")