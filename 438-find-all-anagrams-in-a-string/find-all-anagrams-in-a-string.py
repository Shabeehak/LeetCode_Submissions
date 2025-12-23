class Solution(object):
    def findAnagrams(self, s, p):
        if len(s)<len(p):
            return []
        result = []
        p_count = [0] * 26
        window_count = [0] * 26
        for ch in p:
            p_count[ord(ch)-ord('a')]+=1
        left = 0
        right = 0
        k = len(p)
        while right<len(s):
            window_count[ord(s[right])-ord('a')]+=1
            right+=1
            if right-left==k:
                if window_count == p_count:
                    result.append(left)
                window_count[ord(s[left])-ord('a')]-=1
                left +=1
        return result