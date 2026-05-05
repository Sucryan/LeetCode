# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/solutions/3978548/easy-to-understandfull-explanationdone-i-mtta
# https://chatgpt.com/share/69f9c9c0-0598-83a8-94a4-4143a99d795c
# 這題你可以把它想成：
    # 右邊的人已經排好隊了，左邊每個巨人都要被切成小人，切完不能比右邊第一個人高。切越少越好，所以每次剛好切到「最大塊不超標」就好。
# 這題的貪心精髓就是：
    # 從右往左，每次用最少切割次數，把目前數字壓到右邊能接受的高度。
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        last = nums[n - 1]  # Initialize 'last' with the last element
        ans = 0  # Initialize the total operations count

        # Traverse the array in reverse order
        for i in range(n - 2, -1, -1):
            if nums[i] > last:  # If the current element needs replacement
                t = nums[i] // last  # Calculate how many times the element needs to be divided
                if nums[i] % last:
                    t += 1  # If there's a remainder, increment 't'
                last = nums[i] // t  # Update 'last' for the next comparison
                ans += t - 1  # Add (t - 1) to 'ans' for the number of operations
            else:
                last = nums[i]  # Update 'last' without replacement
        return ans  # Return the total number of operations