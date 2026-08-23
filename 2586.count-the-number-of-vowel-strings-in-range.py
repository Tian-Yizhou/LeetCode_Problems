#
# @lc app=leetcode id=2586 lang=python3
#
# [2586] Count the Number of Vowel Strings in Range
#

# @lc code=start
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in range(left, right+1):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                ans += 1
            else:
                continue

        return ans

# @lc code=end

