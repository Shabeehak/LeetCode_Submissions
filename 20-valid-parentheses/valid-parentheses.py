class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        track = []
        for b in s:
            if b in brackets:
                if track and track[-1]==brackets[b]:
                    track.pop()
                else:
                    return False
            else:
                track.append(b)
        return len(track)==0