class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        from collections import Counter
        count = Counter(nums)
        return [num for num, _ in heapq.nlargest(k, count.items(), key = lambda x: x[1])]