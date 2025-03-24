class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mirror_tree(node):
    if node is None:
        return None
    
    # Swap the left and right subtrees
    node.left, node.right = node.right, node.left
    
    # Recursively mirror the left and right subtrees
    if node.left:
        mirror_tree(node.left)
    if node.right:
        mirror_tree(node.right)
    
    return node

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node is not None:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)



# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal of original tree:")
inorder_traversal(root)
print()

print("Preorder traversal of mirrored tree:")
preorder_traversal(root)


mirror_tree(root)

print()
print("Inorder traversal of mirrored tree:")
inorder_traversal(root)
print()

