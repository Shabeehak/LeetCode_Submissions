class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        window_size = len(p)
        if len(s)<window_size:
            return []
        p_count=[0]*26
        s_count=[0]*26
        for c in p:
            p_count[ord(c)-ord('a')]+=1
        result = []
        left, right = 0, 0
        while right<len(s):
            s_count[ord(s[right])-ord('a')]+=1
            right+=1
            if right-left==window_size:
                if p_count == s_count:
                    result.append(left)
                s_count[ord(s[left])-ord('a')]-=1
                left +=1
        return result    