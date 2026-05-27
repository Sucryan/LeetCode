class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # https://leetcode.com/problems/patching-array/solutions/5319434/easy-to-understand-greedy-approach-detai-ddek
        miss = 1
        result = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                result += 1

        return result