
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_all_paths(node: Node, target_sum: int, parents: list):

    if node is None:
        return 0
    
    parents.append(node.value)
    print_all_paths(node.left, target_sum, parents)
    print_all_paths(node.right, target_sum, parents)

    f = 0
    for i in range(len(parents)-1, -1,-1):
        f += parents[i]
        if f == k:
            #print from this parent to leaf
            for j in range(i, len(parents)):
                print(parents[j], end='')
                
            print()

    parents.pop(-1)




    
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

parents = []
print(print_all_paths(root, k, parents))
