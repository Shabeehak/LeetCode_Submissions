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
        p_count = [0]*26
        x_count = [0]*26
        result = []
        for ch in p:
            p_count[ord(ch)-ord('a')]+=1
        
        left, right = 0, 0
        
        while right<len(s):
            x_count[ord(s[right])-ord('a')]+=1
            right+=1
            if right - left == window_size:
                if p_count == x_count:
                    result.append(left)
                x_count[ord(s[left])-ord('a')]-=1
                left +=1
        return result