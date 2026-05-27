from typing import List
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solutions/8291716/using-min-max-pointers-by-rahulkadvasara-xbgu
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        mn = float('inf')
        f = False

        # Find minimum misplaced element
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                f = True

            if f:
                mn = min(mn, nums[i])

        # Already sorted
        if mn == float('inf'):
            return 0

        f = False
        mx = float('-inf')

        # Find maximum misplaced element
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                f = True

            if f:
                mx = max(mx, nums[i])

        st = -1
        end = -1

        # Find correct starting position
        for i in range(n):
            if nums[i] > mn:
                st = i
                break

        # Find correct ending position
        for i in range(n - 1, -1, -1):
            if nums[i] < mx:
                end = i
                break

        return end - st + 1