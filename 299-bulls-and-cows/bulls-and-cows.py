class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull , cow = 0, 0
        secret_unmatched = []
        guess_unmatched = []
        for i, j in zip(secret, guess):
            if i == j:
                bull+=1
            else:
                secret_unmatched.append(i)
                guess_unmatched.append(j)
        for val in guess_unmatched:
            if val in secret_unmatched:
                cow+=1
                secret_unmatched.remove(val)
            
        return "{}A{}B".format(bull,cow)