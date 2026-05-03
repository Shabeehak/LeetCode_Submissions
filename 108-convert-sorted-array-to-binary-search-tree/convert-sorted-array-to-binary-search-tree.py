# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def bs_convert(nums):
            if not nums:
                return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            node.left = bs_convert(nums[:mid])
            node.right = bs_convert(nums[mid+1:])
            return node
        return bs_convert(nums)