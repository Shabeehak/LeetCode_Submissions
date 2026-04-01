# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        values =[]
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
        inorder(root)
        
        def build(nums):
            if not nums:
                return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            node.left = build(nums[:mid])
            node.right = build(nums[mid+1:])
            return node
        return build(values)