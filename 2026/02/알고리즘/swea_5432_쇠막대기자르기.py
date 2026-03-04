T = int(input())
 
for tc in range(1,T+1):
    stick = input()
 
    stick_num = 0
 
    fragment = 0
 
    i = 0
    while i < len(stick):
        if stick[i:i+2] == '()':
            fragment += stick_num
            i += 2
        elif stick[i] == '(':
            stick_num += 1
            i += 1
        else:
            stick_num -= 1
            fragment += 1
            i += 1
     
    print(f"#{tc} {fragment}")