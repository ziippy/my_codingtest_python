# 이진 탐색 트리 구현

list = [5, 3, 8, 4, 2, 1, 7, 10]
search_list = [1, 2, 5, 6]

class Node:
    def __init__(self, key):
        self.left = None
        self.key = key
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            curr = self.root
            while True:
                if key < curr.key:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = Node(key)
                        break
                elif key > curr.key:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break

    def search(self, key):
        curr = self.root
        while curr and curr.key != key:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
        return True if curr else False

def printBST(node):
    print(node.key)
    if node.left is not None:
        printBST(node.left)
    if node.right is not None:
        printBST(node.right)


bst = BST()
for i in list:
    bst.insert(i)
print(printBST(bst.root))

answer = []
for search in search_list:
    answer.append(bst.search(search))

print(answer)