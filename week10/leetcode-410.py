class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        def ok(X: int) -> bool:
            cur = 0
            cut = 1
            for x in nums:
                if cur + x <= X:
                    cur += x
                else:
                    cut += 1
                    cur = x
                    if cut > k: return False
            return True
        
        while l <= r:
            m = (l + r) // 2
            if ok(m):
                r = m - 1
            else:
                l = m + 1
        return l

            