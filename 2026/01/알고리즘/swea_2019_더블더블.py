N = int(input())
 
result = 1
def dob(n):
    if n == -1:
        return 1
    else:
        global result
        print(result, end=' ')
        result *= 2
        return n * dob(n-1)
     
dob(N)