'''
Author: Hannah
Date: 2026-10-06 09:51:49
LastEditTime: 2026-10-06 11:02:35
'''
#
# @lc app=leetcode id=2516 lang=python3
#
# [2516] Take K of Each Character From Left and Right
#

# @lc code=start
from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Method: sliding window
        # time complexity: O(n + |sigma|)
        # space complexity: O(sigma), sigma=3 is the size of set of char
        # for each right bound, consider what is the longest window
        # to keep characters
        cnt = Counter(s)
        if any(cnt[char] < k for char in "abc"):
            return -1

        max_length = 0
        left = 0
        for right, char in enumerate(s):
            # add current character into window
            cnt[char] -= 1
            while cnt[char] < k:
                cnt[s[left]] += 1
                left += 1
            max_length = max(max_length, right-left+1)

        return len(s) - max_length
        
# @lc code=end

