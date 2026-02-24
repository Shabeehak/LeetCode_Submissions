# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        def dfs(node, depth):
            if not node:
                return
            if len(result)==depth:    #create nested list in each level
                result.append([])
            result[depth].append(node.val)   #add value based on level
            dfs(node.left, depth+1)
            dfs(node.right,depth+1)
        dfs(root,0)
        return result