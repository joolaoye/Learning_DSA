def sumoflevels(root):
    if root is None: return 0

    queue = [root]
    explored = []

    while queue:
        tmp = []
        for _ in range(len(queue)):
            cur = queue.pop(0)

            tmp.append(cur.val)

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

        explored.append(tmp)


    return explored


class TreeNode:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
i = TreeNode(8)
j = TreeNode(9)

a.left, a.right = b,c
b.left,b.right,c.left,c.right = d,e,f,g
d.left,d.right = i,j

print(sumoflevels(a))