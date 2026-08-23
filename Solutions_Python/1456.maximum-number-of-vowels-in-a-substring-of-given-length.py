#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # time complexity: O(n)
        n = len(s)
        ans = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        # initial window
        for i in range(k):
            if s[i] in vowels:
                ans += 1
        left, right = 0, k-1
        cnt = ans
        # the window stops when right == n-1
        while right < n-1:
            # right side: add a letter
            if s[right+1] in vowels:
                cnt += 1
            right += 1
            # left side: move a letter
            if s[left] in vowels:
                cnt -= 1
            left += 1
            # update answer
            ans = max(ans, cnt)

        return ans


        
# @lc code=end

