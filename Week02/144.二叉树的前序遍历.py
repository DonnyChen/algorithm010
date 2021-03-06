#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.pfs(root, res)
        return res

    def pfs(self, root, res):
        if root:
            res.append(root.val)
            self.pfs(root.left, res)
            self.pfs(root.right, res)

# @lc code=end
