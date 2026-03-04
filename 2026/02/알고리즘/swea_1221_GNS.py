T = int(input())
numbers = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9
    }
for tc in range(1,T+1):
    poop, N = input().split()
    lst = input().split()
    lst.sort(key=lambda x: numbers[x])
    print(f"#{tc}")
    print(*lst)