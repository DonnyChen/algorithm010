#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            for i in root.children:
                self.dfs(i, res)

    # https://www.cnblogs.com/captain-dl/p/9588902.html
    def preorder2(self, root: 'Node') -> List[int]:
        ret, q = [], root and [root]
        while q:
            node = q.pop()
            ret.append(node.val)
            q += [child for child in node.children[::-1] if child]

        return ret
# @lc code=end
