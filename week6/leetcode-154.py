from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]: #which means before r we don't have minimum it must be after r so make l = mid+1
                l = mid+1
            elif nums[mid]<nums[r]: #which means minimum must be before or on mid
                r = mid
            else: #when the mid value is same as r value so we can easily decrease r as we have one copy at mid
                r -=1
        return nums[l]

