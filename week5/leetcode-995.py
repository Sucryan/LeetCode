from collections import deque
# https://www.youtube.com/watch?v=Fv3M9uO5ovU
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        res = 0
        for i, num in enumerate(nums):
            while q and (i-q[0]+1) > k:
                q.popleft()
            
            if (len(q)+num)%2 == 0:
                if i+k > len(nums):
                    return -1
                res += 1
                q.append(i)
        return res