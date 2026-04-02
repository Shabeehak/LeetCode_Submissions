class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        missing = []
        i=1
        while count <=k:
            if i not in arr:
                missing.append(i)
                count+=1
            i+=1
        return missing[k-1]
            
