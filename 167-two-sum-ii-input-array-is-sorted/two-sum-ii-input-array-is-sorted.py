class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = dict()
        for i in range(len(numbers)):
            if target-numbers[i] in seen:
                return [seen[target-numbers[i]], i+1]
            else:
                seen[numbers[i]]=i+1
        return False