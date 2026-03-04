for tc in range(1, 11):
    N = int(input())
    st = input()
    new_st = ''
    operator = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 3
    }

    oper_stack = []
    
    for i in range(N):
        if st[i] == ')':
            while oper_stack[-1] != '(':
                new_st += oper_stack.pop()
            oper_stack.pop()
            continue
        if st[i].isdecimal():
            new_st += st[i]
        else:
            if oper_stack and oper_stack[-1] != '(' and operator[oper_stack[-1]] >= operator[st[i]]:
                new_st += oper_stack.pop()
            oper_stack.append(st[i])

    if oper_stack:
        new_st += oper_stack.pop()

    result = 0
    new_st_list = list(new_st)
    for i in range(len(new_st_list)):
        if new_st_list[i].isdecimal():
            new_st_list[i] = int(new_st_list[i])

    i = 0
    while len(new_st_list) > 1:
        if operator.get(new_st_list[i]):
            if new_st_list[i] == '+':
                new_st_list[i-2:i+1] = [new_st_list[i-2] + new_st_list[i-1]]
                i -= 2
                continue
            elif new_st_list[i] == '-':
                new_st_list[i-2:i+1] = [new_st_list[i-2] - new_st_list[i-1]]
                i -= 2
                continue
            elif new_st_list[i] == '*':
                new_st_list[i-2:i+1] = [new_st_list[i-2] * new_st_list[i-1]]
                i -= 2
                continue
            else:
                new_st_list[i-2:i+1] = [new_st_list[i-2] / new_st_list[i-1]]
                i -= 2
                continue
        
        i += 1

    print(f"#{tc} {new_st_list[0]}")