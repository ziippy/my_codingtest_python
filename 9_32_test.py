# 길 찾기

# 좌표 정보가 주어지는데 이걸 가지고 트리를 구성하고, 전방순회/후방순회 길을 출력

nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]

# y 값이 큰걸로 정렬, y 값이 같으면 x 값이 작은걸 우선

class Node:
    def __init__(self, info, num, left=None, right=None):
        self.info = info
        self.num = num
        self.left = left
        self.right = right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None

nodes = [i for i in range(1, len(nodeinfo) + 1)]
print(nodes)
# nodes.sort(key=lambda x: nodeinfo[x - 1][1], reverse=True)  # y 값 내림차순
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [7, 2, 4, 1, 3, 6, 8, 9, 5]
nodes.sort(key=lambda x: (nodeinfo[x - 1][1], -nodeinfo[x - 1][0]), reverse=True) # y 값은 내림차순, x 값은 오름차순
print(nodes)
# [7, 4, 2, 6, 1, 3, 9, 8, 5]

root = None
for i in range(len(nodes)):
    if root is None:
        root = Node(nodeinfo[nodes[0] - 1], nodes[0])
    else:
        parent = root
        node = Node(nodeinfo[nodes[i] - 1], nodes[i])
        #
        while True:
            if node.info[0] < parent.info[0]:
                if parent.has_left():
                    parent = parent.left
                    continue
                parent.left = node
                break
            else:
                if parent.has_right():
                    parent = parent.right
                    continue
                parent.right = node
                break
print(root)

# def preorder(root, answer):
#     stack = [root]
#     while stack:
#         node = stack.pop()
#         if node is None:
#             continue
#         answer.append(node.num)
#         stack.append(node.right)
#         stack.append(node.left)

def preorder(node, answer):
    if node is None:
        return
    answer.append(node.num)
    preorder(node.left, answer)
    preorder(node.right, answer)

# def postorder(root, answer):
#     stack = [(root, False)]
#     while stack:
#         node, visited = stack.pop()
#         if node is None:
#             continue
#         if visited == True:
#             answer.append(node.num)
#         else:
#             stack.append((node, True))
#             stack.append((node.right, False))
#             stack.append((node.left, False))

def postorder(node, answer):
    if node is None:
        return
    postorder(node.left, answer)
    postorder(node.right, answer)
    answer.append(node.num)


preorder_answer = []
preorder(root, preorder_answer)
print(preorder_answer)
# [7, 4, 6, 9, 1, 8, 5, 2, 3]

postorder_answer = []
postorder(root, postorder_answer)
print(postorder_answer)
# [9, 6, 5, 8, 1, 4, 3, 2, 7]


# nodes = {}
# for idx, node in enumerate(nodeinfo):
#     nodes[idx] = node
# print(nodes)

# sorted_nodeinfo = sorted(nodes, key=lambda x: , reverse=True)
# print(sorted_nodeinfo)