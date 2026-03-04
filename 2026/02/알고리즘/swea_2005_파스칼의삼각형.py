for tc in range(1, 11):
    N = int(input())
    st = input()
    my_list = []
    my_dict = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
 
    result = 1
    for i in st:
        if i in ['(', '[', '{', '<']:
            my_list.append(i)
        else:
            if my_list and my_dict[my_list[-1]] == i:
                my_list.pop()
            else:
                result = 0 
                break
    if my_list:
        result = 0
    print(f"#{tc} {result}")