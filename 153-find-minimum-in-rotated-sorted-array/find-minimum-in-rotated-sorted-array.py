class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        l=0
        r=len(nums)-1
        while l<=r:
            if nums[l]<nums[r]: #sorted then left min
                res = min(res, nums[l])
                break
            m = (l+r)//2
            res = min(res, nums[m])
            if nums[m]<=nums[r]: #right sorted
                r = m-1 #go to left
            else: #left sorted
                l = m+1
        return res