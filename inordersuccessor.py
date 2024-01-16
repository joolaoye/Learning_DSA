class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        # Code here
        if root is None: return None

        stack = [root]
        cur = root
        seen = False

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if seen:
                return cur.data

            if cur.data == x.data:
                seen = True

            cur = cur.right

        return None


a = Node(2)
b = Node(1)
c = Node(3)
d = Node(4)

a.left, a.right = b,c
c.left = d

print(Solution().inorderSuccessor(a, a))