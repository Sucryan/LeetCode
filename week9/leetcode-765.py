# https://leetcode.com/problems/couples-holding-hands/solutions/4204660/765-solution-with-step-by-step-explanati-7lr3
# https://chatgpt.com/share/69f9c7cf-73a0-83a2-b421-af4148d05784
# 把每個人轉成 couple id：person // 2。
# 每張雙人椅如果坐了兩個不同 couple，就把這兩個 couple union 起來。
# 每個 connected component 有 k 對情侶，修好需要 k-1 次 swap。
# 所以總答案 = couple 總數 - component 數。
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY

        n = len(row) // 2
        parent = [i for i in range(n)]
        
        for i in range(0, len(row), 2):
            union(row[i] // 2, row[i+1] // 2)
        
        count = sum([1 for i, x in enumerate(parent) if i == find(x)])
        return n - count