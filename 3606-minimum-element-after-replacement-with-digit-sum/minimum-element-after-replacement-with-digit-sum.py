class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0]*len(nums)
        for i,n in enumerate(nums):
            n = str(n)
            sum =0
            for j in range(len(n)):
                sum +=int(n[j])
            res[i] = sum
        return min(res)