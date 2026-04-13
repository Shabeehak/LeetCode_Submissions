class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        result = []
        for i in range(len(nums)):
            if nums[i]==target:
                result.append(abs(i-start))
        return min(result)
            