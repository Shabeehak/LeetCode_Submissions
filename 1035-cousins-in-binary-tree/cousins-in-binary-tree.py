# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        info = dict()
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                info[node.val] = (parent, depth)
            dfs(node.left, node, depth+1) 
            dfs(node.right, node, depth+1)

        dfs(root, None, 0)

        x_parent, x_depth = info[x]
        y_parent, y_depth = info[y]

        return x_parent!=y_parent and x_depth == y_depth