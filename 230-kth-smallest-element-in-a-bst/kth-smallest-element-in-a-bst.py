# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count = [0]
        result = [None]
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            count[0] +=1
            if count[0]==k:
                result[0]=node.val
                return
            inorder_traversal(node.right)
        inorder_traversal(root)
        return result[0]