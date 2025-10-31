class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l]<=nums[m]: #left sorted
                if nums[l]<=target<=nums[m]: #target inside left sorted
                    r = m-1
                else: #taregt in unsorted part
                    l = m+1 
            else: #right sorted
                if nums[m]<=target<=nums[r]: #target inside right sorted
                    l = m+1
                else: #target inside unsorted
                    r = m-1
        return -1
