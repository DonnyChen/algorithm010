#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# If the total is less than zero, we need it to be larger, so we move the left pointer
# If the total is greater than zero, we need it to be smaller, so we move the right pointer.

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
# @lc code=end
