class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def count_paths_from_node(node: Node, target: int, current_sum: int):

    if node is None:
        return 0
    
    paths = 0
    
    current_sum += node.value
    
    if current_sum == target:
        paths += 1


    paths += count_paths_from_node(node.left, target, current_sum)
    paths += count_paths_from_node(node.right, target, current_sum)

    return paths

def count_all_paths(root: Node, target: int):

    if(root is None):
        return 0

    paths = count_paths_from_node(root, target, 0)

    paths += count_all_paths(root.left, target)
    paths += count_all_paths(root.right, target)

    return paths



root = Node(8)
root.left = Node(4)
root.right = Node(5)

root.left.left = Node(3)
root.left.right = Node(2)

root.left.left.left = Node(3)
root.left.left.right = Node(-2)

root.left.right.right = Node(1)

root.right.right = Node(2)

k = 7

print(count_all_paths(root, k))
