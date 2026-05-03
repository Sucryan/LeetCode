class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for i in range(n)]
        # 先從左邊數過去。
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        # 再從右邊數回來
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1]+1, candies[i])
        return sum(candies)