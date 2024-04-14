# tree

nodes = [1, 2, 3, 4, 5, 6, 7]

# 전방순회

def preorder(nodes, idx):
    if idx < len(nodes):
        ret = str(nodes[idx]) + " "
        ret += preorder(nodes, idx * 2 + 1)
        ret += preorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""


def inorder(nodes, idx):
    if idx < len(nodes):
        ret = inorder(nodes, idx * 2 + 1)
        ret += str(nodes[idx]) + " "
        ret += inorder(nodes, idx * 2 + 2)
        return ret
    else:
        return ""

def postorder(nodes, idx):
    if idx < len(nodes):
        ret = inorder(nodes, idx * 2 + 1)
        ret += inorder(nodes, idx * 2 + 2)
        ret += str(nodes[idx]) + " "
        return ret
    else:
        return ""
    
print(preorder(nodes, 0))
print(inorder(nodes, 0))
print(postorder(nodes, 0))