class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def find_depth(node):

    if node is None:
        return 0
    
    print(node.value)

    left_depth = find_depth(node.left)
    right_depth = find_depth(node.right)

    return max(left_depth, right_depth) + 1

def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(8)
root.left = Node(4)
root.right = Node(5)

root.left.left = Node(3)
root.left.right = Node(2)

root.left.left.left = Node(3)
root.left.left.right = Node(-2)

root.left.right.right = Node(1)

root.right.right = Node(2)

#print(find_depth(root))
print(bfs(root))
