def VLR(node):
    if tree.get(node):
        print(node, end='')
        if tree[node][0] != '.':
            VLR(tree[node][0])
        if tree[node][1] != '.':
            VLR(tree[node][1])
    return

def LVR(node):
    if tree.get(node):
        if tree[node][0] != '.':
            LVR(tree[node][0])
        print(node, end='')
        if tree[node][1] != '.':
            LVR(tree[node][1])
    return

def LRV(node):
    if tree.get(node):
        if tree[node][0] != '.':
            LRV(tree[node][0])
        if tree[node][1] != '.':
            LRV(tree[node][1])
        print(node, end='')
    return

N = int(input())
tree = {}
for _ in range(N):
    nodes = input().split()
    tree[nodes[0]] = [nodes[i] for i in range(1,3)]

VLR('A')
print()
LVR('A')
print()
LRV('A')