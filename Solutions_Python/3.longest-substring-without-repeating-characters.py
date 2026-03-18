'''
Author: Hannah
Date: 2026-03-17 19:49:51
LastEditTime: 2026-03-17 20:00:59
'''
#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = Counter()
        left = 0
        ans = 0
        for right, char in enumerate(s):
            cnt[char] += 1
            while cnt[char] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        
        return ans
# @lc code=end

