class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def range_sum_of_bst(root, low, high):
    if root is None:
        return 0

    # Passover the Bianary Search Tree (BST) using DFS (Depth-First Search)
    stack = [root]
    total_sum = 0

    while stack:
        node = stack.pop()

        if node:
            if low <= node.value <= high:
                total_sum += node.value

            # Add right branch first, then left branch (to mimic in-order traversal)
            stack.append(node.right)
            stack.append(node.left)

    return total_sum
