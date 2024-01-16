def post_order(root):
    if root is None: return []

    explored = []
    stack = [[root, False]]

    while stack:
        cur, visited  = stack[-1]

        if not visited:
            stack[-1][1] = True

            if cur.right:
                stack.append([cur.right, False])

            if cur.left:
                stack.append([cur.left, False])

        elif visited:
            explored.append(cur.data)
            stack.pop()

    return explored



class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left, a.right = b,c
c.left, b.left = e,d

print(post_order(a))