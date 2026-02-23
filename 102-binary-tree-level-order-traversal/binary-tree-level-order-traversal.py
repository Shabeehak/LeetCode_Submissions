# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result=[]             #main list to return
        queue = deque([root]) #control over level
        while queue:
            level = []        #sub list to add main list
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)   #here sub list created
                if node.left:
                    queue.append(node.left)   #here next level number of count and value taken
                if node.right:
                    queue.append(node.right)   #here next level number of count and value taken
            result.append(level)  #here main list getting sub list
        return result