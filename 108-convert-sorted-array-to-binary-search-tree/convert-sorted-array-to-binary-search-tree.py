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
        def covrt_bbst(nums):
            if not nums:
                return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            node.left = covrt_bbst(nums[:mid])
            node.right = covrt_bbst(nums[mid+1:])
            return node
        return covrt_bbst(nums)
