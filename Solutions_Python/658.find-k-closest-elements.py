'''
Author: Hannah
Date: 2026-10-01 19:01:57
LastEditTime: 2026-10-01 20:01:49
'''
#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # Method 3: exclude + binary search
        # time complexity: O(log(N-K) + K)
        # space complexity: O(K)
        # use bisect to find the start index of a k length arr
        # assume the start index is mid, then we compare arr[mid] and arr[mid+k]
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            # arr[mid+k] is the first element our of window
            # if arr[mid+k] is closer, we need to move the window to right side: left = mid + 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            # if arr[mid] is closer, we need to move the window to left side, right = mid
            else:
                right = mid
                
        # when left == right, we find the start index of the window
        return arr[left:left + k]


        # Method 2: exclude len(arr)-k elements
        # time complexity: O(N)
        left, right = 0, len(arr) - 1
        # when there are more than len(arr)-k elements
        while right - left + 1 > k:
            # if arr[left] is closer
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            # if arr[right] is closer
            else:
                right -= 1
                
        return arr[left:right + 1]
    
        # Method 1: use bisect to find left and right start index, 
        # then expand from both sides
        left = bisect.bisect_left(arr, x)
        right = bisect.bisect_right(arr, x)
        ans = []
        cnt = 0
        # if x is not in arr
        if left == right:
            if left == 0:
                return arr[:k]
            elif left == len(arr):
                return arr[-k:]
            else:
                left -= 1
        # if left != right, means arr[left:right] are all x
        else:
            if right - left >= k:
                return arr[left:left+k]
            else:
                ans = arr[left:right]
                cnt = right - left
                left -= 1

        # start justify from left and right
        while cnt < k:
            # if left side exceeds the boundary 0
            if left < 0:
                ans.append(arr[right])
                right += 1
            # if right side exceeds the boundary len(arr)-1
            elif right >= len(arr):
                ans.insert(0, arr[left])
                left -= 1
            else:
                val_l, val_r = arr[left], arr[right]
                if abs(val_l - x) <= abs(val_r - x):
                    ans.insert(0, val_l)
                    left -= 1
                else:
                    ans.append(val_r)
                    right += 1
            cnt += 1

        return ans

# @lc code=end

