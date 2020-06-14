#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # version 1 枚举左右边界，求最大面积
        '''length = len(height)
        max_area = 0
        for i in range(length -1):
            for j in range(i+1, length):
                area = (j-i) * min(height[i], height[j])
                max_area = max(max_area, area)

        return max_area'''

        # V2 双指针法
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            cur_area = min(height[left], height[right]) * (right - left)
            area = max(area, cur_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return area
        # @lc code=end
