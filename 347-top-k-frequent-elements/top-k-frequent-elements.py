class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        count = Counter(nums)
        return [item for item, _ in heapq.nlargest(k,count.items(), key = lambda x:x[1])]