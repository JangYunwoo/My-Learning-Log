T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))

    max_height = max(heights)
    
    onetwodays = {
        1: 0,
        2: 0
    }

    need_days = 0
    for i in range(len(heights)):
        onetwodays[2] += (max_height - heights[i]) // 2
        onetwodays[1] += (max_height - heights[i]) % 2
    
    if onetwodays[1] >= onetwodays[2]:
        sub = onetwodays[2]
    else:
        sub = onetwodays[1]

    need_days += sub * 2
    onetwodays[1] -= sub
    onetwodays[2] -= sub

    if onetwodays[1] > onetwodays[2]:
        need_days += onetwodays[1] * 2 - 1
    elif onetwodays[1] < onetwodays[2]:
        need_days += (onetwodays[2] // 3) * 4
        remainder = onetwodays[2] % 3
        if remainder == 1:
            need_days += 2
        elif remainder == 2:
            need_days += 3

    print(f"#{tc} {need_days}")