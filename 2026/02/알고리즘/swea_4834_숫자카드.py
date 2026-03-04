T = int(input())
 
for i in range(T):
    N = int(input())
    a = input()
 
    numbers = [0 for _ in range(10)]
    for j in a:
        numbers[9 - int(j)] += 1
 
    print(f"#{i+1} {9 - numbers.index(max(numbers))} {max(numbers)}")
