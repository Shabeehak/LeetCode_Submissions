class WordDictionary(object):

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node:
                node[char]={}
            node = node[char]
        node['#'] = None
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, i):
            if i == len(word):
                return '#' in node
            char = word[i]
            if char=='.':
                for child in node:
                    if child!='#':
                        if dfs(node[child], i+1):
                            return True
                return False
            if char not in node:
                return False
            return dfs(node[char], i+1)
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)