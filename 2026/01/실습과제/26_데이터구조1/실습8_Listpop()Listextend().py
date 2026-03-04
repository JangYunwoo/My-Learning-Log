# 아래 함수를 수정하시오.
def even_elements(lst):
    A = []
    for _ in range(len(lst)):
        B = lst.pop(0)
        if B % 2 == 0:
            A.extend([B])
    return A

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
