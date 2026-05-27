class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/rotate-function/solutions/8120429/0ms-beats-10000-easy-approach-and-step-b-yr4w
        n = len(nums)
        
        total_sum = 0
        F = 0
        
        for i in range(n):
            total_sum += nums[i]
            F += i * nums[i]
        
        result = F
        
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            result = max(result, F)
        
        return result