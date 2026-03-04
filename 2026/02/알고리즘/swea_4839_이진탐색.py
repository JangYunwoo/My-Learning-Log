T = int(input())
 
for tc in range(T):
    P, Pa, Pb = map(int, input().split())
    ra, rb = P, P
    la, lb = 1, 1
 
    while True:
        ca, cb = int((la+ra)/2), int((lb+rb)/2)
        if ca < Pa:
            la = ca
        else:
            ra = ca
         
        if cb < Pb:
            lb = cb
        else:
            rb = cb
         
        if ca == Pa and cb == Pb:
            result = 0
            break
        elif ca == Pa:
            result = "A"
            break
        elif cb == Pb:
            result = "B"
            break
 
    print(f"#{tc+1} {result}")