class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prev_map = dict() #hash mapping
        for i, num in enumerate(nums):
            if target-num in prev_map:
                return [i, prev_map[target-num]]
            else:
                prev_map[num]=i