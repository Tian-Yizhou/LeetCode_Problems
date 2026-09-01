#
# @lc app=leetcode id=2606 lang=python3
#
# [2606] Find the Substring With Maximum Cost
#

# @lc code=start
import string
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # initialization
        letter_dict = dict(zip(string.ascii_lowercase, range(1, 27)))
        for i, char in enumerate(chars):
            letter_dict[char] = vals[i]

        # Method 3: optimize method 2 space complexity
        # time complexity: O(n)
        # space complexity: O(1)
        # f[i]: the max sub-string sum that ends with s[i]
        ans = 0
        for i, char in enumerate(s):
            if i == 0:
                f = letter_dict[char]
            else:
                f = max(f, 0) + letter_dict[char]
            ans = max(ans, f)

        return ans

    
        # Method 2: dp
        # time complexity: O(n)
        # space complexity: O(n)
        # f[i]: the max sub-string sum that ends with s[i]
        n = len(s)
        ans = 0
        f = [0] * n
        for i, char in enumerate(s):
            if i == 0:
                f[0] = letter_dict[char]
            else:
                f[i] = max(f[i-1], 0) + letter_dict[char]

        return max(max(f), 0)


        # Method 1: pre sum + greedy
        # time complexity: O(n)
        # space complexity: O(n)
        ans = 0
        pre_sum = 0
        min_pre_sum = 0
        for i, char in enumerate(s):
            pre_sum += letter_dict[char]
            ans = max(pre_sum - min_pre_sum, ans)
            min_pre_sum = min(min_pre_sum, pre_sum)

        return ans

# @lc code=end

