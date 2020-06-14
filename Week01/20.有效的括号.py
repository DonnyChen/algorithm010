#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dict1:
                if stack == [] or dict1[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return not stack
# @lc code=end
