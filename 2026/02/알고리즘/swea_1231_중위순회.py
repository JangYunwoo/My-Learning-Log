def inorder(node):
 
    if node*2 <= N:
        inorder(node*2)
    print(tree[node], end="")
 
    if node*2+1 <= N:
        inorder(node*2+1)
 
for tc in range(1, 11):
 
    N = int(input())
    tree = [0]*(N+1)
    for idx in range(1, N+1):
        tree[idx] = input().split()[1]
 
    print(f"#{tc} ",end='')
     
    inorder(1)
    print()