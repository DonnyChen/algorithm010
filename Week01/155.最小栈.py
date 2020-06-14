#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.help_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.help_stack or x <= self.help_stack[-1]:
            self.help_stack.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.help_stack[-1]:
            self.help_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.help_stack[-1]

# @lc code=end
