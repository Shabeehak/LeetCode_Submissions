class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        val = 0
        nums = set(nums)
        if len(nums)>=k:
            for i in range(k):
                val = max(nums)
                res.append(val)
                nums.remove(val)
        else:
            for i in range(len(nums)):
                val = max(nums)
                res.append(val)
                nums.remove(val)
        return res

