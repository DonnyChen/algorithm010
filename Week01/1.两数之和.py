#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in d:
                return d[diff], i
            else:
                d[nums[i]] = i


# @lc code=end
