class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count = dict()
        for char in s:
            if char not in s_count:
                s_count[char]=1
            else:
                s_count[char]+=1
        t_count = dict()
        for char in t:
            if char not in t_count:
                t_count[char]=1
            else:
                t_count[char]+=1
        if s_count == t_count:
            return True
        return False