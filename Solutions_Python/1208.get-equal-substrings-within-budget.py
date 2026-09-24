#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Method: sliding window
        # time complexity: O(n)
        # space complexity: O(n)
        # given a window, if the window cost <= maxCost, then update answer(window length)
        # if the window cost > maxCost, move left side until it's valid
        ans = 0
        left = 0
        curCost = 0
        for right, char in enumerate(s):
            if s[right] != t[right]:
                curCost += abs(ord(s[right]) - ord(t[right]))
                while curCost > maxCost:
                    curCost -= abs(ord(s[left]) - ord(t[left]))
                    left += 1
            # now the sub-string is valid, update answer
            ans = max(ans, right-left+1)

        return ans

# @lc code=end

