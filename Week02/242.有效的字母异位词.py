#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start


class Solution:
    # 1 排序
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)

    # 2 哈希映射
    def isAnagram(self, s: str, t: str) -> bool:
        dict26 = [0]*26
        if len(t) != len(s):
            return False

        for i in range(len(t)):
            dict26[ord(s[i]) - ord('a')] += 1
            dict26[ord(t[i]) - ord('a')] -= 1

        for j in range(26):
            if dict26[j] != 0:
                return False

        return True

# @lc code=end
