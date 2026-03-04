N = int(input())

count = 0
num = 665
while True:
    num += 1
    if str(num).find('666') != -1:
        count += 1
        if count == N:
            print(num)
            break