class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_map = dict()
        for i, val in enumerate(nums):
            if target-val in prev_map:
                return (i, prev_map[target-val])
            else:
                prev_map[val]=i